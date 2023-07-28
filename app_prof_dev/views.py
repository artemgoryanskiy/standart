from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Category, Program


def main_page_view(request):
    return render(request, 'app_prof_dev/main.html', {})


class CategoryListView(ListView):
    model = Category
    template_name = 'app_prof_dev/category_list.html'
    context_object_name = 'categories'


def program_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    programs = Program.objects.filter(category=category)
    context = {'category': category, 'programs': programs}
    return render(request, 'app_prof_dev/program_list.html', context)
