from django.urls import path
from .views import PostListView


app_name = 'app_news'


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
]