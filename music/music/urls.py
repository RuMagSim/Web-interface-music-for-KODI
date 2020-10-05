from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    url(r'', include('music.folder.urls')),	
    ]

