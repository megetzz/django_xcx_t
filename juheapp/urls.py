from django.urls import path,include

from juheapp import views

urlpatterns = [
    path('juhe/',views.hellojuhe),
    path('test/',views.testrequest),
    path('image/',views.image),
    # 类的调用 as_view()
    path('image1/',views.ImageView.as_view()),
    path('imagetext/',views.ImageText.as_view()),
    path('testcookie/',views.CookieTest.as_view()),

    path('',views.apps),
]
