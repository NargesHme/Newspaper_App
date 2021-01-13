from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def str(self):
        return self.title

    def get_absolute_url(self, parameter_list):
        return reverse('article_detail', args=[str(self.id)])