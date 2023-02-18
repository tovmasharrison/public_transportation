from django.urls import path

from . import views

app_name = "transportation"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    
    path('transport-types/', views.transport_types, name = 'types'),
    path('transport-types/<str:t_type>/', views.transport_list, name = 'transportation'),
    path('transport-types/<str:t_type>/<str:pk>/', views.transport_details, name = 'details'),
    
    path('create-transport/', views.create_transport, name = 'create-transport'),
    path('update-transport/<str:pk>/', views.update_transport, name = 'update-transport'),
    path('delete-transport/<str:pk>/', views.delete_transport, name = 'delete-transport'),
    path('about_us/', views.About_us.as_view(), name="about_us")
]
