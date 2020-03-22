from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
# Create your views here.
import requests


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

def image(request):
    f = open(r'D:\PycharmProjects\dj_three\helloword\static\abc.png','rb')
    # return HttpResponse(content=f.read(),content_type='image/png')
    return FileResponse(f,content_type='image/png')