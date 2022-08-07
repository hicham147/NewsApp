from . import views  

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('contact/', views.contect,name='contact'),
    path('about/', views.about,name='about'),
    
]
