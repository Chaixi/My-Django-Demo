from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    source = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    release_time = models.DateTimeField()
    read_status = models.IntegerField()
    get_time = models.DateTimeField()
    imgs = models.CharField(max_length=255)

class jwc_News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    source = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    release_time = models.DateTimeField()
    read_status = models.IntegerField()
    get_time = models.DateTimeField()
    imgs = models.CharField(max_length=255)

class xsc_News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    source = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    release_time = models.DateTimeField()
    read_status = models.IntegerField()
    get_time = models.DateTimeField()
    imgs = models.CharField(max_length=255)