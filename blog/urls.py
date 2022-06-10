from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path('<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
]
