from django.db import models

# Create your models here.

class User(models.Model):
    openid =models.CharField(max_length=64,unique=True)
    nickName = models.CharField(max_length=64)