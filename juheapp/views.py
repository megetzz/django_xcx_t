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
from utils.responseutil import ResponseMixin,XxxxxMixin,UtilMinxin
from django.shortcuts import render
from utils import responseutil
from utils.responseutil import UtilMixin
import  json
from helloword import secret_settings
from juheapp.models import User

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
    print('cookie---->', request.COOKIES)
    # return HttpResponse('========')
    return JsonResponse({'请求方法---->': request.method.__str__(),
                         '客户端信息---->': request.META.__str__(),
                         'get请求参数-->': request.GET.__str__(),
                         '请求头---->': request.headers.__str__(),
                         'cookie---->': request.COOKIES.__str__()
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
        # print('--->',filepath)
    # filepath=r'D:\PycharmProjects\dj_three\helloword\static\abc.png'
    # print('filepath:',filepath)
        f=open(filepath,'rb')
        return FileResponse(f,content_type='image/png')
    elif request.method == 'POST':
        return HttpResponse('这儿是post请求')
    else:
        return HttpResponse('res.method:'+request.method+'没有实现')

# 4 11 单元

# cbv 类试图
class ImageView(View,UtilMinxin):

    def get(self,request):
        filepath=os.path.join(settings.STATIC_ROOT_SELF,'abc.png')
        f=open(filepath,'rb')
        return FileResponse(f,content_type='image/jpg')
        # return render(request,'upfile.html')


    def post(self,request):
        # return HttpResponse('这儿是post请求')
        # file_obj = request.FILES.get('file',None)
        # print(file_obj.name)
        # print(file_obj.size)
        # print(dir(request))
        files1 = request.FILES
        # print('>>>>>>>>>>>>>>>>',files1)
        # print('--->',files1)
        # picdir = settings.UPLOAD_PIC_DIR
        # files = request.FILES
        # print(type(files))
        # django.utils.datastructures.MultiValueDict
        # 鸭子模式
        # for key, value in files1.item:
        picdir = settings.UPLOAD_PIC_DIR

        for key, value in files1.items():
            filename = os.path.join(picdir,key[-32:])
            # UtilMinxin.savepic(key[-8:],value.read())
            UtilMinxin.savepic(filename,value.read())
            print('----->',key)
            print('--->',value)
        # return HttpResponse(filename)
        return JsonResponse(UtilMinxin.wrapdic({'filename-':key[-32:]}))
        # filename = key
        # return self.get(request)
        #     filename = os.path.join(picdir,key[-8:])

        # return HttpResponse('ceshi')
        # return HttpResponse(filename)


    def delete(self,request):
        picname = request.GET.get('name')
        print('picname:',picname)
        picdir = settings.UPLOAD_PIC_DIR
        pic_full_path = os.path.join(picdir,picname)
        if not os.path.exists(pic_full_path):
            return HttpResponse('图片不存在')
        else:
            # 删除
            os.remove(pic_full_path)
            return HttpResponse('图片删除成功')
        # return HttpResponse('删除成功')
    # def put(self,request):
        # return HttpResponse('put请求')
        # return self.get(request)

from utils import responseutil
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
#         response = {}
#         response['code']=1000
#         response['codedes']='返回成功,没问题'
#         return response

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
    filepath = r'/home/pluto/django_xcx_t/helloword/myappconfig.yaml'
    with open(filepath,'r',encoding='utf8') as f:
        res = yaml.load(f,Loader=yaml.FullLoader)
    return JsonResponse(res,safe=False)

# 获取cookie 并保存到本地
class CookieTest(View):
    """
    此视图对应的路由是http://127.0.0.1:8000/api/v1.0/apps/testcookie/
    """
    def get(self,request):
        # print(dir(request))
        request.session['mykey']='我的值'
        return JsonResponse({'key':'value'})

# 读取本地cookie并发送cookie
class CookieTest2(View):
    """
    此视图对应的路由是http://127.0.0.1:8000/api/v1.0/apps/testcookie2/
    负责接受cookie
    """
    def get(self,request):
        # request.session  字典
        # print(request.session['mykey'])
        print(request.session['mykey'])
        print(request.session.items())
        return JsonResponse({'key2':'value2'})

# 请求地址
# https://api.weixin.qq.com/sns/jscode2session
# ?appid=APPID
# &secret=SECRET
# &js_code=JSCODE
# &grant_type=authorization_code


# 认证登录se
class Authorize(View):
    def get(self,request):
        return HttpResponse('此接口不支持get')

    def post(self,request):
        print(request.body)
        #b'{"code":"033eAyih1vHypv0gH1hh1Neqih1eAyiS"}'
        bodystr = request.body.decode('utf-8')
        bodydict = json.loads(bodystr)
        code = bodydict.get('code')
        nickName = bodydict.get('nickName')
        print('code--->',code)
        print('nickName---->',nickName)
        appid = secret_settings.APPID
        secret = secret_settings.SECTRY_KEY
        js_code = code
        # 发起请求  从微信发过来的额
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(appid,secret,js_code)
        res = requests.get(url)
        # print(res.text)

        res_dict = json.loads(res.text)
        openid = res_dict.get('openid')
        if not openid:
            return HttpResponse('Authorize fail')
        # 给用户赋予状态 session和其他东西关联
        request.session['openid'] = openid
        request.session['is_authorized'] = True


        # 将用户保存到本地 的 数据库
        if not User.objects.filter(openid=openid):
            newuser = User(openid=openid, nickName=nickName)
            newuser.save()

        return HttpResponse('Authorize post ok')




# def __authorize_by_code(request):
#     '''
#     使用wx.login的到的临时code到微信提供的code2session接口授权
#
#     post_data = {
#         'encryptedData': 'xxxx',
#         'appId': 'xxx',
#         'sessionKey': 'xxx',
#         'iv': 'xxx'
#     }
#     '''
#     response = {}
#     post_data = request.body.decode('utf-8')
#     post_data = json.loads(post_data)
#     app_id = post_data.get('appId').strip()
#     nickname = post_data.get('nickname').strip()
#     code = post_data.get('code').strip()
#     print(code)
#     print(app_id)
#     if not (app_id and code):
#         response['result_code'] = 2500
#         response['message'] = 'authorized failed. need entire authorization data.'
#         return JsonResponse(response, safe=False)
#     try:
#         data = c2s(app_id, code)
#     except Exception as e:
#         print(e)
#         response['result_code'] = 2500
#         response['message'] = 'authorized failed.'
#         return JsonResponse(response, safe=False)
#     openid = data.get('openid')
#     if not openid:
#         response['result_code'] = 2500
#         response['message'] = 'authorization error.'
#         return JsonResponse(response, safe=False)
#     request.session['openid'] = openid
#     request.session['is_authorized'] = True
#
#     print(openid)
#     # User.objects.get(openid=openid) # 不要用get，用get查询如果结果数量 !=1 就会抛异常
#     # 如果用户不存在，则新建用户
#     if not User.objects.filter(openid=openid):
#         new_user = User(openid=openid, nickname=nickname)
#         new_user.save()
#
#     # message = 'user authorize successfully.'
#     # response = wrap_json_response(data={}, code=ReturnCode.SUCCESS, message=message)
#     return JsonResponse(response, safe=False)
#
#
# def authorize(request):
#     return __authorize_by_code(request)
#
#
# class UserView(View):
#     # 关注的城市、股票和星座
#     def get(self, request):
#         if not already_authorized(request):
#             return JsonResponse({'key': '没登录认证'}, safe=False)
#         openid = request.session.get('openid')
#         user = User.objects.get(openid=openid)
#         data = {}
#         data['focus'] = {}
#         data['focus']['city'] = json.loads(user.focus_cities)
#         data['focus']['stock'] = json.loads(user.focus_stocks)
#         data['focus']['constellation'] = json.loads(user.focus_constellations)
#         return JsonResponse(data=data, safe=False)
#         pass
#
#     def post(self, request):
#         if not already_authorized(request):
#             return JsonResponse({'key': '没登录认证'}, safe=False)
#         openid = request.session.get('openid')
#         user = User.objects.get(openid=openid)
#
#         received_body = request.body.decode('utf-8')
#         received_body = eval(received_body)
#
#         cities = received_body.get('city')
#         stocks = received_body.get('stock')
#         constellations = received_body.get('constellation')
#         #  不是追加的形式,是覆盖原有纪录
#         # todo 这个bug 可以自己修复下
#         # 前后端配合 更全面的逻辑,做更少的事,更健壮的事
#         # 前端每次加载界面时,获取数据,和新添加的数据混合,保存时都post到后台
#         # 后台只需要覆盖数据
#
#         user.focus_cities = json.dumps(cities)
#         user.focus_stocks = json.dumps(stocks)
#         user.focus_constellations = json.dumps(constellations)
#         user.save()
#
#         return JsonResponse(data={'msg': '成功了'}, safe=False)
#         pass
#

#
# class CookieTest(View):
#     """
#     此视图对应的路由是 http://127.0.0.1:8000/api/v1.0/apps/testcookie/
#     """
#
#     def get(self, request):
#         # print(dir(request)) session
#         request.session['mykey'] = '我的值'
#         return JsonResponse({'key': "value"})
#
#
# class CookieTest2(View):
#     """
#     此视图对应的路由是 http://127.0.0.1:8000/api/v1.0/apps/testcookie2/
#     负责接收cookie
#     """
#
#     def get(self, request):
#         # request.session 是个字典
#         # print(dir(request)) session
#         print(request.session['mykey'])
#         print(request.session.items())
#         return JsonResponse({'key2': "value2"})
#
#
# class Authorize(View):
#     def get(self, request):
#         return HttpResponse('此接口不支持get')
#
#     def post(self, request):
#         print(request.body)  # b'{"code":"071D7x2705Z2nC1KQ6470hiA270D7x2F"}'
#         bodystr = request.body.decode('utf-8')
#         bodydict = json.loads(bodystr)
#         code = bodydict.get('code')
#         nickName = bodydict.get('nickName')
#         print(code)
#         print(nickName)
#         appid = secret_settings.APPID
#         secret = secret_settings.SECTER_KEY
#         js_code = code
#
#         # 发起请求
#         url = 'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(
#             appid, secret, js_code)
#         res = requests.get(url)
#         # print(res.text)
#         res_dict = json.loads(res.text)
#         openid = res_dict.get('openid')
#         if not openid:
#             return HttpResponse('Authorize fail')
#         # 给这个用户赋予了一些状态
#         request.session['openid'] = openid
#         request.session['is_authorized'] = True
#
#         # 将用户保存到 咱们的数据库
#         if not User.objects.filter(openid=openid):
#             newuser = User(openid=openid, nickname=nickName)
#             newuser.save()
#
#         return HttpResponse('Authorize post ok')
#
#
# GET https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code
def c2s(appid, code):
    return code2session(appid, code)
#
#
def code2session(appid, code):
    API = 'https://api.weixin.qq.com/sns/jscode2session'
    params = 'appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % \
             (secret_settings.APPID, secret_settings.SECTRY_KEY, code)
    url = API + '?' + params
    response = requests.get(url=url, )
    data = json.loads(response.text)
    print(data)
    return data
#
#
def __authorize_by_code(request):
    '''
    使用wx.login的到的临时code到微信提供的code2session接口授权

    post_data = {
        'encryptedData': 'xxxx',
        'appId': 'xxx',
        'sessionKey': 'xxx',
        'iv': 'xxx'
    }
    '''
    response = {}
    post_data = request.body.decode('utf-8')
    post_data = json.loads(post_data)
    app_id = post_data.get('appId').strip()
    nickname = post_data.get('nickname').strip()
    code = post_data.get('code').strip()
    print(code)
    print(app_id)
    if not (app_id and code):
        response['result_code'] = 2500
        response['message'] = 'authorized failed. need entire authorization data.'
        return JsonResponse(response, safe=False)
    try:
        data = c2s(app_id, code)
    except Exception as e:
        print(e)
        response['result_code'] = 2500
        response['message'] = 'authorized failed.'
        return JsonResponse(response, safe=False)
    openid = data.get('openid')
    if not openid:
        response['result_code'] = 2500
        response['message'] = 'authorization error.'
        return JsonResponse(response, safe=False)
    request.session['openid'] = openid
    request.session['is_authorized'] = True

    print(openid)
    # User.objects.get(openid=openid) # 不要用get，用get查询如果结果数量 !=1 就会抛异常
    # 如果用户不存在，则新建用户
    if not User.objects.filter(openid=openid):
        new_user = User(openid=openid, nickname=nickname)
        new_user.save()

    # message = 'user authorize successfully.'
    # response = wrap_json_response(data={}, code=ReturnCode.SUCCESS, message=message)
    return JsonResponse(response, safe=False)


def authorize(request):
    return __authorize_by_code(request)


# 判断是否已经授权
# 从session得出字段
def already_authorized(request):
    is_authorized = False
    if request.session.get('is_authorized'):
        is_authorized = True
    return is_authorized


def get_user(request):
    if not already_authorized(request):
        raise Exception('not authorized request')
    openid = request.session.get('openid')
    user = User.objects.get(openid=openid)
    return user


class UserView(View):
    # 关注的城市、股票和星座
    def get(self, request):
        if not already_authorized(request):
            return JsonResponse({'key': '没登录认证'}, safe=False)
        openid = request.session.get('openid')
        user = User.objects.get(openid=openid)
        data = {}
        data['focus'] = {}
        data['focus']['city'] = json.loads(user.focus_cities)
        data['focus']['stock'] = json.loads(user.focus_stocks)
        data['focus']['constellation'] = json.loads(user.focus_constellations)
        return JsonResponse(data=data, safe=False)


    def post(self, request):
        if not already_authorized(request):
            return JsonResponse({'key': '没登录认证'}, safe=False)
        openid = request.session.get('openid')
        user = User.objects.get(openid=openid)

        received_body = request.body.decode('utf-8')
        received_body = eval(received_body)

        cities = received_body.get('city')
        stocks = received_body.get('stock')
        constellations = received_body.get('constellation')
        #  不是追加的形式,是覆盖原有纪录
        # todo 这个bug 可以自己修复下
        # 前后端配合 更全面的逻辑,做更少的事,更健壮的事
        # 前端每次加载界面时,获取数据,和新添加的数据混合,保存时都post到后台
        # 后台只需要覆盖数据

        user.focus_cities = json.dumps(cities)
        user.focus_stocks = json.dumps(stocks)
        user.focus_constellations = json.dumps(constellations)
        user.save()


        return JsonResponse(data={'msg': '成功了'}, safe=False)

#
#注销
class Logout(View):
    def get(self, request):
        # 清除session
        request.session.clear()
        return JsonResponse(data={'key': 'logout'}, safe=False)
#
#获取状态
class Status(View):
    # 判断是否已经登陆
    def get(self, request):
        print('call get_status function...')
        if already_authorized(request):
            # 1 成功
            data = {"is_authorized": 1}
        else:
            data = {"is_authorized": 0}
        return JsonResponse(data, safe=False)

def weather(cityname):
    '''
    根据城市得到天气
    :param cityname: 城市名字
    :return: 返回实况天气
    '''
    key =  secret_settings.KEY
    api = 'http://apis.juhe.cn/simpleWeather/query'
    params = 'city=%s&key=%s' % (cityname[:-1], key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url)
    data = json.loads(response.text)
    print(data)
    result = data.get('result')
    realtime = result.get('realtime')
    response = {}
    response['temperature'] = realtime.get('temperature')
    response['wid'] = realtime.get('wid')
    response['power'] = realtime.get('power')
    response['humidity'] = realtime.get('humidity')
    # response = {}
    # response['temperature'] = 'temperature'
    # response['win'] = 'win'
    # response['humidity'] = 'humidity'
    return response
#

class Weather(View):
    def get(self, request):
        if not already_authorized(request):
            response = {'key':2500}
        else:
            data = []
            openid = request.session.get('openid')
            user = User.objects.filter(openid=openid)[0]
            cities = json.loads(user.focus_cities)
            for city in cities:
                result = weather(city.get('city'))
                result['city_info'] = city
                data.append(result)
            response = data
        return JsonResponse(data=response, safe=False)


    def post(self, request):
        data = []
        received_body = request.body.decode('utf-8')
        received_body = json.loads(received_body)
        print(received_body)
        cities = received_body.get('cities')
        for city in cities:
            result = weather(city.get('city'))
            result['city_info'] = city
            data.append(result)
        response_data = data
        return JsonResponse(data=response_data, safe=False)

# def weather(cityname):
#     '''
#     根据城市得到天气
#     :param cityname: 城市名字
#     :return: 返回实况天气
#     '''
#     key = 'e8cf055e940444f46092ac9c2abc6db5'
#     api = 'http://apis.juhe.cn/simpleWeather/query'
#     params = 'city=%s&key=%s' % (cityname[:-1], key)
#     url = api + '?' + params
#     print(url)
#     response = requests.get(url=url)
#     data = json.loads(response.text)
#     print(data)
#     result = data.get('result')
#     realtime = result.get('realtime')
#     response = {}
#     response['temperature'] = realtime.get('temperature')
#     response['wid'] = realtime.get('wid')
#     response['power'] = realtime.get('power')
#     response['humidity'] = realtime.get('humidity')
#     # response = {}
#     # response['temperature'] = 'temperature'
#     # response['win'] = 'win'
#     # response['humidity'] = 'humidity'
#     return response
#
# #
# class Weather(View):
#     def get(self, request):
#         if not already_authorized(request):
#             response = {'key':2500}
#         else:
#             data = []
#             openid = request.session.get('openid')
#             user = User.objects.filter(openid=openid)[0]
#             cities = json.loads(user.focus_cities)
#             for city in cities:
#                 result = weather(city.get('city'))
#                 result['city_info'] = city
#                 data.append(result)
#             response = data
#         return JsonResponse(data=response, safe=False)
#
#     def post(self, request):
#         data = []
#         received_body = request.body.decode('utf-8')
#         received_body = json.loads(received_body)
#         print(received_body)
#         cities = received_body.get('cities')
#         for city in cities:
#             result = weather(city.get('city'))
#             result['city_info'] = city
#             data.append(result)
#         response_data = {'key':'post..'}
#         return JsonResponse(data=response_data, safe=False)