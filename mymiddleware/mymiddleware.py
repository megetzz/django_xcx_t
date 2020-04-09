import time
import logging
import json
logger_statistics = logging.getLogger('statistics')

class TestMiddle():

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('before call')
        print(request)
        response = self.get_response(request)
        print('after call')
        return response


class StatisticsMiddle():

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('before call')
        start_time = time.time()
        print(request)
        path = request.path
        # full_path = request.get_full_path()
        response = self.get_response(request)
        end_time = time.time()
        print('after call')
        # todo  将时间戳转成具体时间
        log_dict = {
            'start_time':start_time,
            'used_time':end_time - start_time,
            'path':path,
            # 'full_path':full_path,
            'end_time':end_time
        }
        # end_time - start_time path
        logger_statistics.info(repr(log_dict))
        return response


