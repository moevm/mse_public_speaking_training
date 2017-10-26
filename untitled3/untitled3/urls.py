
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('landing.urls')),
]


