from django.shortcuts import render
from django.views.generic import DetailView
from .models import ProductEco


class ProductDetailView(DetailView):
    model = ProductEco
    context_object_name = 'product'
    template_name = 'app_ecology/product_detail.html'


def main_eco_page_view(request):
    return render(request, 'app_ecology/main_ecology.html', context={})