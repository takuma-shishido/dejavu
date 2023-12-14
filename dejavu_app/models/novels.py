from django.db import models

class Novels(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=255)
    introdiction = models.CharField(max_length=255)
    user_id = models.IntegerField()

    def __str__(self):
        return self.title