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
    path('testcookie2/',views.CookieTest2.as_view()),
    path('authorize/',views.Authorize.as_view()),
    path('user/',views.UserView.as_view()),
    path('logout/',views.Logout.as_view()),
    path('status/',views.Status.as_view()),
    path('weather/',views.Weather.as_view()),

    path('',views.apps),
]
