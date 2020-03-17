from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Article

def index(request):
    return HttpResponse("Hello,world,'首页,新的应用'.")

def show_detail(request):
    first_article=Article.objects.all()[0]

    return HttpResponse(first_article.title)

# 一个
def show_article(request):
    first_article=Article.objects.all()[0]
    return render(request,'show.html',{'article':first_article})

# 两个
def show_article2(request):
    article=Article.objects.all()[0]
    # first_article=Article.objects.all()[0]
    first_article1=Article.objects.all()[1]
    return render(request,'show2.html',{'article':article,'article1':first_article1})

# 全部
def show_articles(request):
    articles=Article.objects.all()
    return render(request,'shows.html',{'articles':articles})