from django.db import models
from django.contrib.auth.models import User

class Novels(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255)
    user_id = models.IntegerField()

    def __str__(self):
        return self.title