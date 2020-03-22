from django.urls import path,include

from juheapp import views

urlpatterns = [
    path('juhe/',views.hellojuhe),
    path('test/',views.testrequest),
    path('image/',views.image),
]