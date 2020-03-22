from django.db import models

# Create your models here.

class Article(models.Model):
    article_id=models.AutoField(primary_key=True)
    title=models.TextField()
    brief_content=models.TextField()
    content=models.TextField()
    publist_date=models.DateTimeField(auto_now=True)

# 在后台界面显示
    def __str__(self):
        return self.title