from django.urls import path,include

import app1.views

urlpatterns = [
    path('hello_world',app1.views.hello_world)
]