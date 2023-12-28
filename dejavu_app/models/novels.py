from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Novels(models.Model):
    STATUS_DEVELOPMENT = 0 # 承
    STATUS_TURN = 1        # 転
    STATUS_CONCLUSION = 2  # 結

    STATUS_CHOICES = [
        (STATUS_DEVELOPMENT, '承'),
        (STATUS_TURN, '転'),
        (STATUS_CONCLUSION, '結'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default=1)
    title = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_DEVELOPMENT)

    def __str__(self):
        return self.title