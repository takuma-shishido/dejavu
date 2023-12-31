from django.db import models

class NovelMaster(models.Model):
    STATUS_DEVELOPMENT = 1 # 承
    STATUS_TURN = 2        # 転
    STATUS_CONCLUSION = 3  # 結

    STATUS_CHOICES = [
        (STATUS_DEVELOPMENT, 'Development'),
        (STATUS_TURN, 'Turn'),
        (STATUS_CONCLUSION, 'Conclusion'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_DEVELOPMENT)

    def __str__(self):
        return self.status