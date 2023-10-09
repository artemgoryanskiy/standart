from django.urls import path
from .views import PostListView, PostDetailView


app_name = 'app_news'


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]