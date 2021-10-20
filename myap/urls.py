from django.contrib import admin
from django.urls import path
from myap import views

urlpatterns = [
    path("" , views.home , name='home'),
    path("posts" , views.posts , name='posts'),
]
