from django.db import models
from dejavu_app.models.novel_master import NovelMaster

class NovelDetail(models.Model):
    user_id = models.IntegerField()
    novel_id = models.IntegerField()
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content