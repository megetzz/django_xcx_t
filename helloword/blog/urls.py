from django.urls import path,include
from blog import views

urlpatterns = [
    path('hello/',views.hello),
    path('show/',views.show_detail),
    path('show_article/',views.show_article),
    path('show_article2/',views.show_article2),
    path('show_articles/',views.show_articles),
    path('index/',views.index),
    path('detail/<int:article_id>',views.detail2),
    path('image/',views.show_image),
    # path('detail2/<int:article_id>',views.detail2)
]