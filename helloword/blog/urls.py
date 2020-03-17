from django.urls import path,include
from blog import views

urlpatterns = [
    path('hello/',views.index),
    path('show/',views.show_detail)
]