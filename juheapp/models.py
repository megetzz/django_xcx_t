from django.db import models

# Create your models here.

class User(models.Model):
    openid =models.CharField(max_length=64,unique=True)
    # 昵称
    nickName = models.CharField(max_length=64)
    # 城市
    focus_cities = models.TextField(default='[]')
    # 股票
    focus_constellations = models.TextField(default='[]')
    # 星座
    focus_stocks = models.TextField(default='[]')