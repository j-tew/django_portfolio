from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wargame/', views.war, name='war'),
    path('calculator/', views.calc, name='calc'),
    ]
