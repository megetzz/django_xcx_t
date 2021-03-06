"""helloword URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
# import blog.views
import blog
import app1
import helloword

# import juheapp
# include()就是将其他地方的配置导入
urlpatterns = [
    path('admin/', admin.site.urls),
    # app1
    # path('index/',include("app1.urls")),
    path('app1/',include('app1.urls')),
    # index -->blog  博客
    path('blog/',include('blog.urls')),
    # 聚合api
    path('api/v1.0/',include('helloword.v1_0')),
]


# 在生产环境下才起作用,在开发环境下没用
handler404 = blog.views.not_find_page