from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView
from django.views.generic.edit import UpdateView,DeleteView
from .models import Article
# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'all_articles'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', 'author',)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ('title', 'body',)
