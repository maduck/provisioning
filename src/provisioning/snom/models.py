from django.db import models
from provisioning.base.models import Phone

valid_languages = (
    ('German', 'German'),
    ('English', 'English'),
)
valid_key_modes = (
    (, ),
)

class SnomPhone(models.Model):
    phone = models.ForeignKey(Phone)
    ringtone = models.URLField()
    language = models.ChoicesField(valid_languages)
    user_realname = models.CharField()
    user_name = models.CharField()
    user_host = models.CharField()

class SnomKey(models.Model):
    phone = models.ForeignKey(Phone)
    key = models.PositiveIntegerField()
    function = models.CharField()
