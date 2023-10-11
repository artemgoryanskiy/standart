from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from app_prof_retraining.models import CategoryProfRetrain, ProgramProfRetrain


def education_prof_retr_category_view(request):
    prof_retr_courses = CategoryProfRetrain.objects.all().order_by('-rate')
    paginator = Paginator(prof_retr_courses, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'prof_retr_courses': prof_retr_courses,
        'page_obj': page_obj,

    }
    return render(request, 'education_templates/education_prof_retr.html', context=context)


def education_prof_retr_course_view(request, category_slug):
    category = get_object_or_404(CategoryProfRetrain, slug=category_slug)
    programs = ProgramProfRetrain.objects.select_related('category').filter(category=category)
    context = {'category': category, 'programs': programs}
    return render(request, 'education_templates/education_prof_retr_detail.html', context=context)
