# 把本地的方法提到公用的方法
def wrap_response(response):
    response['code'] = 1000
    response['codedes'] = '返回成功,没问题'
    return response

# 状态码

class Code:
    SUCCESS = 2000
    FAILED = 2222
    @classmethod
    def des(cls,code):
        if code == cls.SUCCESS:
            return 'success ok'
        elif code == cls.FAILED:
            return 'fail not ok'
        else:
            return 'it .....'



# Mixin 提供某些功能的类
class ResponseMixin():
    @staticmethod
    def wrap_response(response):
        # 没有状态码
        if not response.get('code'):
            response['code'] = Code.SUCCESS
        # 没有描述信息
        if not response.get('codedes'):
            response['codedes'] = Code.des(response.get('code'))
        return response

class XxxxxMixin():
    pass