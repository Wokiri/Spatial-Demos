from django.contrib.gis import admin
from .models import RetailStore

admin.site.register(RetailStore, admin.OSMGeoAdmin)
