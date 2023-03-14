# Public Transportation 

## Introduction

  This is a project for the Public Transportation in Armenia to help people find the appropriate Transports for their route by searching or viewing all the transportations and their details and also allows users to rate a specific Transport,leave a review, like a review and add comments to it. The goal of this project is to improve the quality of public transportation by allowing the users to leave reviews and get a better reach.
  The information regarding to the transportation type, number and route are being constantly checked and updated by using CELERY.
  
 Project is written in Django 4.1.6 and Python 3.


## Features

* Create, Update, Delete Tranportations for Superuser

* Rate, Review, Like, Comment

* Google Authentication

* User Registration(Username/Email), Login, 
  Password Change and Reset Through Email

* Celery, Redis

* Web Scrapper and PDF Extractor for Transport Information

* PostgreSQL Database

* ...


## Usage

Clone the repository from GitHub:

$ git clone git@github.com/USERNAME/{{ project_name }}.git

Activate the virtualenv for your project.

Install project dependencies:

$ pip install -r requirements.txt

Then simply apply the migrations:

$ python manage.py migrate

To be able to use the Google Authentication run the server as shown below and navigate to https://publictransport.com:8000

$ python manage.py runserver_plus --cert-file cert.crt

To use the Celery task, run Celery Worker and Celery Beat:

$ celery -A final_project worker -B -l info






