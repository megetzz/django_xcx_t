# 支持类模块

from logging import Filter
class XXXFilter(Filter):
    def filter(self, record):
        # 带 某个的不输出
        if 'z' in record.msg:
            return  False
        else:
            return True