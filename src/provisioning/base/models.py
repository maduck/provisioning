from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    mac = models.CharField(max_length=12)
