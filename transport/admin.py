from django.contrib import admin

from .models import Review, Transportation


# Register your models here.
@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    list_display = ["number", "type"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["name", "rate", "transport"]
    raw_id_fields = ["name", "transport"]
