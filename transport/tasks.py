import os

import pdfplumber
import requests
from bs4 import BeautifulSoup
from django.conf import settings

from final_project.celery import app
from transport.models import Transportation


class Parser:
    """ Class for downloading the pdf files via the link and extracting the appropriate informations """

    url = "https://www.yerevan.am/hy/route-network/"

    pdf_files = ["bus.pdf", "microbus.pdf", "trolleybus.pdf"]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    def download_pdf(self):
        """ downloads the pdf files from the link """

        response = requests.get(self.url, headers=self.headers).text
        soup = BeautifulSoup(response, "lxml")
        hrefs = soup.find("div", class_="description-section").find_all("p")[1:]
        pdf_urls = [href.find("a")["href"] for href in hrefs]
        for i, pdf_file in enumerate(self.pdf_files):
            data = requests.get("https://www.yerevan.am/" + pdf_urls[i], headers=self.headers)
            pdf_path = os.path.join(settings.BASE_DIR, 'transport', pdf_file)
            with open(pdf_path, "wb") as f:
                f.write(data.content)
                self.extract_pdf(pdf_path)

    def extract_pdf(self, pdf_path):
        """ Extracts the downloaded pdf files and creates or updates objects of transportation into the database """

        data = {}
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    for row in table[1:]:
                        if row[1] is not None:
                            key = row[0].strip().replace("\n", "").replace("24ERTUX", "24")
                            if key == "":
                                continue
                            value = row[1].strip().replace("\n", ""). \
                                                   replace("AYIN CANC - 2023-kayq-mikro", "")
                            data[key] = value.strip()
            for key, value in data.items():
                number, route = key.split("\n")[0].strip(), value
                transport_type = pdf_path.split("/")[-1].split(".")[0]
                Transportation.objects.update_or_create(number=number, route=route, type=transport_type)

    def main(self):
        """ Deletes the pdf files and calls download_pdf to download the new ones """

        app_dir = os.path.dirname(os.path.abspath(__file__))
        for file in os.listdir(app_dir):
            if file.endswith(".pdf"):
                os.remove(os.path.join(app_dir, file))
        self.download_pdf()


@app.task
def run_parser():
    """ Celery task for running the Parser class based on a schedule """

    parser = Parser()
    parser.main()
