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




