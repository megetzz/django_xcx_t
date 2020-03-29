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

    def __str__(self):
        return self.nickName

    class Meta:
        """
        meta:  元   描绘类本身的类
        此处描绘user本身的属性
        默认 appname_classname
        默认的索引规则:
        主键必是索引
        外键默认是索引
        唯一也是索引

        索引:提高查询速度
        """

        # db_table = 'abc'
        indexes = [
            # 也是数组
            models.Index(fields=['nickName'],name='nickname'),
            # models.Index(fields=['first_name'],name='first_name_idx')
        ]



