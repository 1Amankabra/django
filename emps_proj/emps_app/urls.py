from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
   
    path('page1/',home1),
    path('page2/',home2)
    
]
