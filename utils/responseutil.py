# 把本地的方法提到公用的方法
def wrap_response(response):
    response['code'] = 1000
    response['codedes'] = '返回成功,没问题'
    return response

# 状态码

class Code:
    SUCCESS = 1000
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


class UtilMinxin():
    @staticmethod
    def savepic(filename, content):
        with open(filename, 'wb') as f:
            f.write(content)
    @staticmethod
    def wrapdic(res_dict):
        """
        返回状态码以及结果,1000 default
        :param res_dict:  需要包裹的返回值字典类型
        :return: 装饰之后的dict
        """
        # with open(filename, 'wb') as f:
        #     f.write(content)
        if not res_dict.get('code'):
            res_dict['code']=Code.SUCCESS
        if not res_dict.get('codedes'):
            res_dict['codedes'] = Code.des(res_dict.get('code'))
        return res_dict
