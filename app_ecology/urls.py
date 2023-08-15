from django.urls import path
from .views import ProductDetailView, main_eco_page_view


app_name = 'app_ecology'

urlpatterns = [
    path('', main_eco_page_view, name='main_eco'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail')
]