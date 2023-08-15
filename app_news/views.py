from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import PostNews


class PostListView(ListView):
    model = PostNews
    context_object_name = 'posts'
    template_name = 'app_news/news_list.html'


class PostDetailView(DetailView):
    model = PostNews
    context_object_name = 'post'
    template_name = 'app_news/news_detail.html'

