from django.db import models
from provisioning.base.models import Phone

class SnomSettings(models.Model):
    phone = models.ForeignKey(Phone)
