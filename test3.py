import  os
import time
import django

# 缓存模块
from django.core.cache import cache

os.environ.setdefault('DJANGO_SETTINGS_MODULE','helloword.settings')
django.setup()

def basic_use():
    s = 'Hello World,hello dajngo Cache'
    cache.set('key',s)
    cache_result = cache.get('key')
    print(cache_result)
    s2 = 'Hello world,hello django Timeout Cache.'
    cache_result = cache.get('key2')
    print(cache_result)
    # time.sleep(5)
    # cache_result = cache.get('key2')
    # print(cache_result)


def get2():

    time.sleep(5)
    res = cache.get('可乐')
    print('res',res)

if __name__ == '__main__':
    # basic_use()
    # get2()
    cache.set('可乐','百事可乐',5)
    print('begin......')
    print(cache.get('可乐'))

    get2()