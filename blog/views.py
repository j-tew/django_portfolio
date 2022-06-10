from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.

class ArticleList(ListView):
    template_name = 'blog/article_list.html'
    model = Article
    context_object_name = 'blog_articles'

class ArticleDetail(DetailView):
    template_name = 'blog/article_detail.html'
    model = Article
    context_object_name = 'article'
