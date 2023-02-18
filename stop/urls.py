from django.urls import path
from . import views
app_name = 'stops'

urlpatterns = [
    path('regions/', views.regions, name = 'regions'),
    path('<str:region>/', views.region_stops, name = 'region-stops' ),
    path('bus-stop/<str:pk>/', views.stop_details, name = 'stop-details'),
    
    path('stops/create-stop/', views.create_stop, name = 'create_stop'),
    path('update-stop/<str:pk>/', views.update_stop, name = 'update-stop'),
    path('delete-stop/<str:pk>/', views.delete_stop, name = 'delete-stop'),
    ]