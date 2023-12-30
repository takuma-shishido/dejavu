from . import novel_detail
from django.utils import timezone
from django.db import models

# class Novel_detail(models.Model):
#     novel_master_id = models.IntegerField()
#     user_id = models.IntegerField()
#     novel_id = models.IntegerField()
#     content = models.CharField(max_length=255)
    # def __str__(self):
    #     return self.novel_id

class Test_blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.TextField(verbose_name='内容')
    postdate = models.DateField(auto_now_add=True, verbose_name='投稿日')

class Comments(models.Model):
    user_id = models.IntegerField(default=0)
    novel_id = models.ForeignKey(Test_blog, on_delete=models.CASCADE, verbose_name='対象小説')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    comment = models.TextField('本文')
    
    def __str__(self):
        return self.comment
    
