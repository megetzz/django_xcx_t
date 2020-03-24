from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
# Create your views here.
import requests
import yaml
from django.conf import settings
# import helloword.settings
# from helloword import settings
import os
from django.views import View
from django.shortcuts import render
# from utils import responseutil
from utils.responseutil import ResponseMixin,XxxxxMixin


# fbv
def hellojuhe(request):
    url = 'http://v.juhe.cn/joke/content/list.php?sort=asc&page=20&pagesize=20&time=1014466512&key=ccea89c0e0afc91fe1f4db1e233d474d'
    res = requests.get(url)
    if res.status_code == 200:
        return HttpResponse(res.text)
    else:
        return HttpResponse('亲,没有获取到数据哦')
    # return  HttpResponse('聚合数据')


def testrequest(request):
    print('请求方法---->', request.method)
    print('客户端信息---->', request.META)
    print('get请求参数-->', request.GET)
    print('请求头---->', request.headers)
    print('cookies---->', request.COOKIES)
    # return HttpResponse('========')
    return JsonResponse({'请求方法---->': request.method.__str__(),
                         '客户端信息---->': request.META.__str__(),
                         'get请求参数-->': request.GET.__str__(),
                         '请求头---->': request.headers.__str__(),
                         'cookies---->': request.COOKIES.__str__()
                         })

# def image(request):
#     f = open(r'D:\PycharmProjects\dj_three\helloword\static\abc.png','rb')
#     return FileResponse(f,content_type='image/png')
    # return HttpResponse(content=f.read(),content_type='image/png')

# 返回图片的请求
# 各种请求的实现
def image(request):
    if request.method == 'GET':
    # static_file_path=settings.STATICFILES_DIRS
    # print('static_file_path',static_file_path)
    # filename=f'/abc.png'
    # filepath=os.path.join(static_file_path,filename)
    # print(filepath)
    # filepath = os.path.join(settings.BASE_DIR,'static','abc.png')
        filepath=os.path.join(settings.STATIC_ROOT_SELF,'abc.png')
        print('--->',filepath)
    # filepath=r'D:\PycharmProjects\dj_three\helloword\static\abc.png'
    # print('filepath:',filepath)
        f=open(filepath,'rb')
        return FileResponse(f,content_type='image/png')
    elif request.method == 'POST':
        return HttpResponse('这儿是post请求')
    else:
        return HttpResponse('res.method:'+request.method+'没有实现')

# cbv 类试图
class ImageView(View):

    def get(self,request):
        filepath=os.path.join(settings.STATIC_ROOT_SELF,'abc.png')
        f=open(filepath,'rb')
        return FileResponse(f,content_type='image/jpg')

    def post(self,request):
        # return HttpResponse('这儿是post请求')
        return self.get(request)

    def put(self,request):
        # return HttpResponse('put请求')
        return self.get(request)

# from utils import responseutil
class ImageText(View,ResponseMixin,XxxxxMixin):
    # def get(self,request):
    #     filepath = os.path.join(settings.STATIC_ROOT_SELF, 'abc.png')
    #     if os.path.exists(filepath):
    #         f = open(filepath, 'rb')
    #         return FileResponse(f, content_type='image/jpg')
    #     else:
    #         return JsonResponse(data={'code':4040,'des':'没有找到图片'})

    # 图片加文子
    # def get(self,request):
    #     return render(request,'imagetext.html',{'des':'图片描述','url':'/api/v1.0/apps/image/'})

# 提取公共的状态信息  本地
#     def wrapjson(self,response):
        # response = {}
        # response['code']=1000
        # response['codedes']='返回成功,没问题'
        # return response

    def get(self,request):
        # return JsonResponse(data={'url':'xxxxxxx','des':'欧克🆗',
        #                           'code':1000,'codedes':'返回成功,没问题'})
        # return JsonResponse(data=self.wrapjson({'url':'xxxxxxx','des':'欧克🆗'}))
        # return JsonResponse(data=responseutil.wrap_response({'url':'xxxxxxx','des':'欧克🆗'}))

# wrap_response 为什么不独立出来,变成一个类,让所有的xxxView 都继承
        return JsonResponse(data=self.wrap_response({'url':'xxxxuibklxxx','des':'我很好','code':2002}))

# def apps(request):
#     return JsonResponse(['微信','支付宝','qq'],safe=False)


# def apps(request):
#     return JsonResponse({'name':['微信','支付宝','顶顶']},safe=True)


# def apps(request):
#     return JsonResponse([{'name':'微信'},{'name':'支付宝'},{'name':'顶顶'}],safe=False)

def apps(request):
    if request.method == 'POST':
        return HttpResponse('逗你玩..')
    filepath = r'D:\PycharmProjects\dj_three\helloword\helloword\myappconfig.yaml'
    with open(filepath,'r',encoding='utf8') as f:
        res = yaml.load(f,Loader=yaml.FullLoader)
    return JsonResponse(res,safe=False)