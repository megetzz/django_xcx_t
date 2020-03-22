from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Article

from django.core.paginator import Paginator

# 返回前端界面
# 纯字符串
def hello(request):
    return HttpResponse("Hello,world,'首页,新的应用'.")



#读取数据库,return个字符串
def show_detail(request):
    first_article=Article.objects.all()[0]

    return HttpResponse(first_article.title)

# 一个  读数据库+模板 渲染   请求+页面+字典
def show_article(request):
    first_article=Article.objects.all()[0]
    return render(request,'show.html',{'article':first_article})

# 两个
def show_article2(request):
    first_article=Article.objects.all()[0]
    first_article1=Article.objects.all()[1]
    return render(request,'show2.html',{'article':first_article,'article1':first_article1})

# django 的模板和 flask的jinja2 模板,使用方式一致

# 全部
def show_articles(request):
    # articles是一个集合, for 循环读取
    articles=Article.objects.all()
    return render(request, 'blog/shows.html', {'articles':articles})


def index(request):
    page=request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    print('page---->',page)
    articles=Article.objects.all()
    # top3_article_list 最近添加的文章
    top3_article_list = Article.objects.order_by('-publist_date')[:3]
    # top3_article_list=Article.objects.order_by('-publist_date')[:3]
    # Paginator  分页的
    p=Paginator(articles,5)     #每页几篇文章
    page_num=p.num_pages

    # print('几页?',page_num)

    # 获取第几页的文章
    page_article_list=p.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page-1
    else:
        previous_page = page
    return  render(request,'blog/index.html',
                   {
                   #     'articles':articles,
                       'articles':page_article_list,
                       'page_num':range(1,page_num + 1 ),
                       'curr_page':page,
                       'next_page':next_page,
                       'previous_page':previous_page,
                       'top3_article_list':top3_article_list
                   })


def detail(request,article_id):
    articles = Article.objects.all()
    cur_article = None
    for article in articles:
        if article.article_id == article_id:
            cur_article = article
            break
    return render(request,'blog/detail.html',{
        'article':cur_article
    })


def detail2(request, article_id):
    articles = Article.objects.all()
    cur_article = None
    previous_article_index = 0
    next_article_index = 0

    previous_article = None
    next_article = None
    # 得到当前文章的id
    # 如果用户随意输入了一个不存在的id ? 怎么办
    for article_index, article in enumerate(articles):
        previous_article_index = article_index - 1
        next_article_index = article_index + 1
        if article_index == 0:
            previous_article_index = 0
        elif article_index == len(articles) - 1:
            next_article_index = len(articles) - 1

        # if article_index==0:
        #     previous_article_index=0
        #     next_article_index=article_index+1
        # elif article_index==len(article)-1:
        #     previous_article_index=article_index-1
        #     next_article_index=len(article)-1
        # else:
        #     previous_article_index = article_index - 1
        #     next_article_index = article_index + 1

        # 确认当前文章是存在于数据库中的
        if article.article_id == article_id:
            cur_article = article
            # 根据上一页文章的id 获取到文章
            previous_article = articles[previous_article_index]
            next_article = articles[next_article_index]
            break
        # else:  # 不存在于数据库中
        #     if article_id > len(articles) - 1:
        #         cur_article = articles[len(articles) - 1]
        #         previous_article = articles[len(articles) - 2]
        #         next_article = articles[len(articles) - 1]
    return render(request, 'blog/detail2.html',
                  {
                      'article': cur_article,
                      'previous_article': previous_article,
                      'next_article': next_article,
                  })



# def detail2(request,article_id):
#     articles = Article.objects.all()
#     cur_article = None
#     previous_article_index = 0
#     next_article_index  = 0
#
#     previous_article = None
#     next_article = None
#     # 得到当前用户的id
#     # 如果输入的id不存在,怎么搞
#     for article_index,article in enumerate(articles):
#         previous_article_index = article_index - 1
#         next_article_index = article_index + 1
#         if article_index == 0:
#             previous_article_index = 0
#         elif article_index == len(articles) - 1:
#             next_article_index = len(articles) - 1
#
#
#         # if article_index == 0:
#         #     previous_article_index=0
#         # elif article_index == len(article)-1:
#         #     previous_article_index = article_index-1
#         #     next_article_index = len(article)-1
#         # else:
#         #     previous_article_index = article_index - 1
#         #     next_article_index = article_index + 1
#
#
#         # 确认当前文章存在数据库
#         if article.article_id == article_id:
#             cur_article =article
#             # 根据上一页的id 获取到文章
#             previous_article = articles[previous_article_index]
#             next_article = articles[next_article_index]
#             break
#         # 不存在数据库
#         # else:
#         #     if article_id > len(articles) - 1:
#         #         cur_article = articles[len(articles)-1]
#         #         previous_article = articles[len(articles)-2]
#         #         next_article = articles[len(articles)-1]
#     return render(request,'blog/detail2.html',{
#         'articles':cur_article,
#         'previous_article':previous_article,
#         'next_article':next_article,
#     })

def not_find_page(request,exception):
    # return HttpResponse('界面没找到')
    return render(request,'blog/page404.html')

from django.http import HttpResponseRedirect
def show_image(request):
    return render(request,'showimage.html')
    # return HttpResponseRedirect