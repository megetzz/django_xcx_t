from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Article

def index(request):
    return HttpResponse("Hello,world,'首页,新的应用'.")

def show_detail(request):
    first_article=Article.objects.all()[0]

    return HttpResponse(first_article.title)