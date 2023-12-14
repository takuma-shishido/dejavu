from django.db import models

class Users(models.Model):
    title = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    def __str__(self):
        return self.title