from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    ##path('', include('selina01.urls')),
    path('', include('mapapi.urls')),
]