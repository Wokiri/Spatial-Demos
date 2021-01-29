from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.

class ReadyServiceManager(models.Manager):
    def get_queryset(self):
        return super(ReadyServiceManager, self).get_queryset().filter(status='ready')

STATUS_CHOICES = (
        ('wait', 'Wait'),
        ('ready', 'Ready'),
    )

class Service(models.Model):
    title = models.CharField(max_length=250)
    details = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='wait')
    order = models.IntegerField()

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title

    objects = models.Manager() # The default manager.
    ready = ReadyServiceManager() # Custom manager.



class Article(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    articleContent = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='wait')
      

    def __str__(self):
        return self.title

    ready = ReadyServiceManager() # Custom manager.


class Project(models.Model):
    title = title = models.CharField(max_length=25)
    details = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # thumbnail = models.ImageField()
    project_url = models.TextField()

    def __str__(self):
        return self.title