from django.urls import path
from django.views.decorators.cache import cache_page

from .views import lab_prot_view

app_name = 'app_lab_prot'

urlpatterns = [
    path('<slug:slug>/', cache_page(60*24)(lab_prot_view), name='lab_prot'),
]
