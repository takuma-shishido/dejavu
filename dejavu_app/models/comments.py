from django.db import models

class Comments(models.Model):
    user_id = models.UUIDField()
    novel_id = models.IntegerField()
    comment = models.CharField(max_length=255)
    def __str__(self):
        return self.novel_id