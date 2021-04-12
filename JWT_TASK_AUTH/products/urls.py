from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('products' , ProductView.as_view() ),
    path('user' , DemoView.as_view()),
]
