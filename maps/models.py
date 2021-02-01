from django.contrib.gis.db import models

class CountriesZones(models.Model):
    name = models.CharField(max_length=254)
    iso = models.CharField(max_length=254)
    zone = models.FloatField()
    colormap = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self): return self.name



class WorldCities(models.Model):
    city = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    region = models.CharField(max_length=254)
    accentcity = models.CharField(max_length=254)
    geom = models.PointField(srid=4326)

    def __str__(self): return self.accentcity