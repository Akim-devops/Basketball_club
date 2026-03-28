from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('secret-entrance-777/', admin.site.urls),
    path('', include('main.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
