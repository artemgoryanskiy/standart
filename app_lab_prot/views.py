from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'app_lab_prot/product_detail.html'


def lab_prot_main_view(request):
    return render(request, 'app_lab_prot/main_lab_prot.html', context={})
