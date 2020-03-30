from django.test import TestCase

# Create your tests here.


# 先配置django的环境
import os
import django
# dajngo黄静的模型
os.environ['DJANGO_SETTINGS_MODULE'] = 'helloword.settings'
django.setup()

from juheapp.models import User,App


user1 = User.objects.all()[0]
print(user1.menu)


# import yaml
# #
# # filepath = r'D:\PycharmProjects\dj_three\helloword\helloword\myappconfig.yaml'
# # with open(filepath,'r',encoding='utf8') as f:
# #     res = yaml.load(f, Loader=yaml.FullLoader)
# #     print(res)
# #     print(type(res))
# #
# #
# # from django.conf import settings
# #
# # os.environ['DJANGO_SETTINGS_MODULE']='helloword.settings'
# # # static_file_path = os.path.join(settings.BASE_DIR,'static')
# # #
# # # print('static_file_path',static_file_path)
# # # filename=r'/abc.png'
# # # filepath= os.path.join(static_file_path,filename)
# # # print(filepath)
# #
# # print('basedir:',settings.BASE_DIR)
# #
# # static_filedir = settings.STATIC_URL
# # # print('static_filedir',static_filedir)
# # print('static_filedir',os.path.join(settings.BASE_DIR,'static'))
# # print(settings.STATIC_ROOT_SELF)
#
#
# # 查询某个对象
# # 导入django的模型
# from juheapp.models import User
#
# # r = User.objects.filter(nickName__contains='ch')
# # r = User.objects.get(nickName='charon@')
# # print(r)
#
# import random
#
# def ranstr(length):
#     CHS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
#     salt = ''
#     for i in range(length):
#         salt += random.choice(CHS)
#     return salt
#
# # print(ranstr(8))
#
# # 增删改查
#
# # 单个增加
# def add_one():
#     # 1
#     # user = User(openid = 'test_open_id', nickName='test_nickname')
#     # user.save()
#
#     # 2
#     User.objects.create(openid = 'test_open_id2', nickName='test_nickname2')
#
# # add_one()
#
# def add_batch():
#     new_user_list = []
#     for i in range(10):
#         open_id = ranstr(32)
#         nickname = ranstr(10)
#         user = User(openid=open_id, nickName=nickname)
#         new_user_list.append(user)
#     User.objects.bulk_create(new_user_list)
#
# # add_batch()
#
# # 查询
# # 精确查询  属性+值
# def get_one():
#             try:
#                 user = User.objects.get(openid='阿斯弗')
#                 print(user)
#             except Exception as e:
#                 print(e)
#
#
# # get_one()
#
# # 数据过滤  模糊查询
# def get_filter():
#     # 属性__哪种类型的模糊查询 __contains包含  __exact 精确
#     users = User.objects.filter(openid__startswith='test')
#     # open_id__startswith
#     # 大于: open_id__gt(greater than)
#     # 小于: open_id__lt(little than)
#     # 大于等于：open_id__gte(greater than equal)
#     # 小于等于：open_id__lte(little than equal)
#     print(users)
#
# # get_filter()
#
#
# # 数据排序
# def get_order():
#     users = User.objects.order_by('nickName')
#     print(users)
#
#
# # get_order()
#
#
# # 连锁查询
# # 和管道符类似
# def get_chain():
#     users = User.objects.filter(openid__contains='test_').order_by('openid')
#     print(users)
#
# # get_chain()
#
# # 改一个
# def modify_one():
#     user = User.objects.get(openid = 'test_open_id')
#     user.nickName = 'modify_username'
#     user.save()
#     # print(user)
#
# # modify_one()
#
# # 批量改
# def modify_batch():
#     User.objects.filter(openid__contains='test_').update(nickName='modify_uname')
#
#
# # modify_batch()
#
# # 删除 一个
# def delete_one():
#     User.objects.get(openid='test_open_id').delete()
#
# # delete_one()
#
# # 批量删除
#
# # 批量删除
# def delete_batch():
#     User.objects.filter(openid__contains='test_').delete()
#
# # delete_batch()
#
# # 全部删除
# def delete_all():
#     User.objects.all().delete()
#
# # 数据库函数
# # 字符串拼接：Concat
#
# from django.db.models import Value
# from django.db.models.functions import Concat
# # annotate创建对象的一个属性, Value可以随便写,如果不是对象中原有属性会报错
# def concat_function():
#     users = User.objects.filter(openid='test_open_id').annotate(
#         # open_id=(open_id), nickName=(nickname)
#         # screen_name = Concat(
#         #     Value('openid='),
#         #     'openid',
#         #     Value(', '),
#         #     Value('nickName='),
#         #     'nickName')
#         # )
#         screen_name = Concat(
#             Value('openid='),'nickName'
#         ))
#     print('screen_name = ', users[0].screen_name)
#
#
# # concat_function()
#
# # 字符串长度
# from django.db.models.functions import Length
#
# def length_function():
#     user = User.objects.filter(openid='test_open_id').annotate(
#         openid_length = Length('openid'))[0]
#
#     print(user.openid_length)
#
# # length_function()
#
#
# # 大小写函数
# from django.db.models.functions import Upper, Lower
#
# def case_function():
#     user = User.objects.filter(openid='test_open_id').annotate(
#         upper_openid=Upper('openid'),
#         lower_openid=Lower('openid')
#     )[0]
#     print('upper_openid:', user.upper_openid, ', lower_openid:', user.lower_openid)
#     pass
#
# # case_function()
#
#
# # 日期处理函数
# # Now()
#
# from blog.models import Article
# from django.db.models.functions import Now
# from datetime import datetime,timedelta
# dt = datetime(day=29,year=2020,month=2)
# print(dt)
# def now_function():
#     # 当前日期之前发布的所有应用
#     # gt  大于
#     # lt 小于
#     # 有 e  equel==
#     articles = Article.objects.filter(publist_date__gt=dt)
#     for article in articles:
#         print(article)
#
# # now_function()
#
# # 时间截断函数
# # Trunc
# from django.db.models import Count
# from django.db.models.functions import Trunc
#
#
# def trunc_function():
#     # 打印每一天发布的应用数量
#     # articel_per_day = Article.objects.annotate(publish_day=Trunc('publist_date', 'month'))\
#     #     .values('publist_date')\
#     #     .annotate(publish_num=Count('article_id'))
#     #
#     # for article in articel_per_day:
#     #     print('date:', article['publist_date'], ', publish num:', article['publish_num'])
#
#     article_per_day = Article.objects.annotate(publish_day = Trunc('publist_date','month'))\
#         .values('publish_day')\
#         .annotate(publish_num = Count('content'))
#         # .annotate(publish_num = Count('article_id'))
#
#     for article in article_per_day:
#         print('date:',article['publish_day'],',publish nums:',article['publish_num'])
#
#
# # trunc_function()
#
# # def addarticle():
# #     Article.objects.create(title='zzz',brief_content='zxx',content='sdfagfg rgasd',publist_date=dt)
# # addarticle()
#
#
# from django.db.models import Q
# from django.db.models import F
#
# # Q 用于构造复杂的查询条件 如  & | 操作
# # ~Q 全部
# def getfilter2():
#     users = User.objects.filter(Q(openid__contains='IeELdFoPqBOdB4tJkktg6gJ9N1ihrjWB') & Q(nickName__contains='test') | Q(nickName__contains='names'))
#     # users = User.objects.filter(~Q(nickName__contains='test'))
#     print(users)
#
#
# # getfilter2()