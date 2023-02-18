from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , include("transport.urls", namespace="transport")),
    path("user/", include("user.urls")),
    path("feedback/", include("feedback.urls", namespace="feedback")),
    path("stops/", include("stop.urls", namespace="stops"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)