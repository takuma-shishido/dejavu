from django.db import models
from dejavu_app.models.novel_master import NovelMaster

class NovelDetail(models.Model):
    novel_master_id = models.IntegerField(choices=NovelMaster.STATUS_CHOICES, default=NovelMaster.STATUS_DEVELOPMENT)
    user_id = models.IntegerField()
    novel_id = models.IntegerField()
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.novel_id