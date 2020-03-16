from django.http import HttpResponse

def index(request):
    return HttpResponse("hello,world  首页")

