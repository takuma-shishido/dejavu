from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Novels(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default=1)
    title = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255)
    # number = models.IntegerField(default=1)

    def __str__(self):
        return self.title