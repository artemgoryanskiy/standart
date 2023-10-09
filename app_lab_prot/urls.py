from django.urls import path
from .views import ProductDetailView, lab_prot_main_view


app_name = 'app_lab_prot'

urlpatterns = [
    path('', lab_prot_main_view, name='lab_prot_main'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail')
]