from django.db import models

class NovelMaster(models.Model):
    status = models.IntegerField()

    def __str__(self):
        return self.status