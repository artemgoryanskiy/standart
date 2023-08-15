from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import CategoryProfTrain, ProgramProfTrain


class CategoryListView(ListView):
    model = CategoryProfTrain
    template_name = 'app_prof_training/category_list.html'
    context_object_name = 'categories'


def program_list(request, category_slug):
    category = get_object_or_404(CategoryProfTrain, slug=category_slug)
    programs = ProgramProfTrain.objects.filter(category=category)
    context = {'category': category, 'programs': programs}
    return render(request, 'app_prof_training/program_list.html', context)