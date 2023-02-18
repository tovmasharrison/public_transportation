from django.db import models
from django.urls import reverse


class BusStop(models.Model):
    class Type(models.TextChoices):
        ARAGATSOTN = "aragatsotn", "Aragatsotn"
        ARARAT = "ararat", "Ararat"
        ARMAVIR = "armavir", "Armavir"
        GEGHARQUNIQ = "gegharquniq", "Gegharquniq"
        LORY = "lory", "Lory"
        KOTAYQ = "kotayq", "Kotayq"
        SHIRAK = "shirak", "Shirak"
        SYUNIK = "syunik", "Syunik"
        VAYOTS_DZOR = "vayots dzor", "Vayots Dzor"
        TAVUSH = "tavush", "Tavush"
        YEREVAN = "yerevan", "Yerevan"
    location = models.CharField(max_length=200)
    letter = models.CharField(max_length = 2, default = '')
    region = models.CharField(max_length = 20, choices = Type.choices, default='yerevan')
    
    def __str__(self):
        return self.location
    
    
    def get_absolute_url(self):
        return reverse('stops:region-stops', kwargs={'region' : self.region})
    
    