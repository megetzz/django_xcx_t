import django
import os
import logging
# from juheapp.models import User,App
os.environ['DJANGO_SETTINGS_MODULE'] = 'helloword.settings'
django.setup()



def logdemo():
    # 得到配置的实例对象
    logger = logging.getLogger('django')
    logger.info('I am log Info')
    logger.info('I am zz log Info')
    logger.warning('I am zz warning log Info')
    logger.warning('I am  warning log Info')
    logger.error('I am zz error log Info')
    logger.error('I am  error log Info')

if __name__ == '__main__':
    logdemo()




# class TimeTestTool:
#     # 计算函数运行的时间
#     @classmethod
#     def calc_func_time(cls, func):
#         start = time.perf_counter()
#         func()
#         end = time.perf_counter()
#         return end - start
#
#     # 统计时间
#     @classmethod
#     def statistic_run_time(cls, func, n):
#         data = [cls.calc_func_time(func) for i in range(n)]
#         mean = statistics.mean(data)
#         sd = statistics.stdev(data, xbar=mean)
#         return [data, mean, sd, max(data), min(data)]
#
#     # 对比
#     @classmethod
#     def compare(cls, func1, func2, n):
#         result1 = cls.statistic_run_time(func1, n)
#         result2 = cls.statistic_run_time(func2, n)
#         print('对比\t 没有预加载 \t 预加载')
#         print('平均值\t', result1[1], '\t', result2[1])
#
#
# # 懒加载
# def lazy_load():
#     for user in User.objects.all():
#         print(user.menu.all())
#
# # 预加载
# def pre_load():
#     for user in User.objects.prefetch_related('menu'):
#         print(user.menu.all())
#
#
# TimeTestTool.compare(lazy_load,pre_load,1000)