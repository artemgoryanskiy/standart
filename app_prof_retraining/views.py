from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import CategoryProfRetrain, ProgramProfRetrain


class CategoryListView(ListView):
    model = CategoryProfRetrain
    template_name = 'app_prof_retraining/category_list.html'
    context_object_name = 'categories'


def program_list(request, category_slug):
    category = get_object_or_404(CategoryProfRetrain, slug=category_slug)
    programs = ProgramProfRetrain.objects.filter(category=category)
    context = {'category': category, 'programs': programs}
    return render(request, 'app_prof_retraining/program_list.html', context)
