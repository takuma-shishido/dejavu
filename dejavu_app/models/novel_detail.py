from django.db import models

class NovelDetail(models.Model):
    novel_master_id = models.IntegerField()
    user_id = models.IntegerField()
    novel_id = models.IntegerField()
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.novel_id