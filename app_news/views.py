from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app_news/news_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'app_news/news_detail.html'

