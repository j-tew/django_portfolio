from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title