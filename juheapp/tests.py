from django.test import TestCase

# Create your tests here.

import os


import yaml

filepath = r'D:\PycharmProjects\dj_three\helloword\helloword\myappconfig.yaml'
with open(filepath,'r',encoding='utf8') as f:
    res = yaml.load(f, Loader=yaml.FullLoader)
    print(res)
    print(type(res))


from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE']='helloword.settings'
# static_file_path = os.path.join(settings.BASE_DIR,'static')
#
# print('static_file_path',static_file_path)
# filename=r'/abc.png'
# filepath= os.path.join(static_file_path,filename)
# print(filepath)

print('basedir:',settings.BASE_DIR)

static_filedir = settings.STATIC_URL
# print('static_filedir',static_filedir)
print('static_filedir',os.path.join(settings.BASE_DIR,'static'))
print(settings.STATIC_ROOT_SELF)