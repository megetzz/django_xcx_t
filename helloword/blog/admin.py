from django.contrib import admin
from .models import Article
# Register your models here.

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title','content','brief_contet','publist_date']
#
#
#
#
# admin.site.register(Article,ArticleAdmin)


# Register your models here.
class ArticleAdimin(admin.ModelAdmin):
    list_display = ['title', 'content','brief_content', 'publist_date']


admin.site.register(Article, ArticleAdimin)