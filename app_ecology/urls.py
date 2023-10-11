from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ecology_view


app_name = 'app_ecology'

urlpatterns = [
    path('<slug:slug>/', cache_page(60*24)(ecology_view), name='ecology'),
]
