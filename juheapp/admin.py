from django.contrib import admin
from juheapp.models import App,User
import random
import time

# Register your models here.



# admin.site.register(User)
admin.site.register(App)

# 这个装饰器相当于admin.site.register(模型类,类名)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 和include相反,不显示某属性
    exclude = ['openid']


# 定义一些规则来控制后台插入模型字段的值
    def save_model(self, request, obj, form, change):
        obj.openid = obj.nickName + str(random.randint(1, 1000))
        print('obj---------->',obj)

        return super(UserAdmin,self).save_model(request, obj, form, change)




# admin
# 后台管理模块
# createsuperuser
# modes -->  定义模型的地方
# admin -->  把模型注册到后台的地方,不注册不在后台显示这个类
# 可读性好 --> 重写模型中的str

# useradmin 类(继承自admin.ModelAdmin)中 fields exclude... 控制后台显示不显示某种字段

# 自定义某些字段的生成规则:
    # 重写useradmin中的 save_model()方法