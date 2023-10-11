from django.urls import path
from .views import news_list_view, news_detail_view


app_name = 'app_news'


urlpatterns = [
    path('', news_list_view, name='news'),
    path('news/<slug:slug>/', news_detail_view, name='news_detail'),
]
