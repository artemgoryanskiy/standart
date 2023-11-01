from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from app_prof_training.forms import BannerSearchForm
from app_prof_training.models import CategoryProfTrain, ProgramProfTrain


def education_prof_train_category_view(request):
    prof_train_courses = CategoryProfTrain.objects.all().order_by('-rate')
    paginator = Paginator(prof_train_courses, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = BannerSearchForm()
    context = {
        'prof_train_courses': prof_train_courses,
        'form': form,
        'page_obj': page_obj,
    }
    return render(request, 'education_templates/education_prof_train.html', context=context)


def education_prof_train_course_view(request, category_slug):
    category = get_object_or_404(CategoryProfTrain, slug=category_slug)
    programs = ProgramProfTrain.objects.select_related('category').filter(category=category)
    context = {'category': category, 'programs': programs}
    return render(request, 'education_templates/education_prof_train_detail.html', context=context)
