from django.contrib.gis.db import models


class Customer(models.Model):

    FOOD_OPTIONS = [
        ('fries', 'fries'),
        ('pizza', 'pizza'),
        ('yams', 'yams'),
    ]

    name = models.CharField(max_length=25, unique=True)
    fav_food = models.CharField(max_length=10, choices=FOOD_OPTIONS, default='fries')
    location = models.PointField(srid=4326)

    class Meta:
        ordering = ["name"]

    def __str__(self): return self.name


class RetailStore(models.Model):

    name = models.CharField(max_length=25)
    description = models.CharField(max_length=125)
    location = models.PointField(srid=4326)

    def __str__(self): return self.name



class NairobiConstituency(models.Model):
    name = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = "constituencies"

    def __str__(self): return self.name



class StoreCustomer(models.Model):
    name = models.CharField(max_length=50)
    geom = models.MultiPointField(srid=4326)

    def __str__(self): return self.name