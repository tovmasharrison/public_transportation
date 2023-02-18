from django.contrib import admin

from .models import BusStop
# Register your models here.
@admin.register(BusStop)
class TransportationAdmin(admin.ModelAdmin):
    list_display = ["location", "region"]
