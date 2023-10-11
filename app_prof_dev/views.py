from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from app_prof_dev.models import CategoryProfDev, ProgramProfDev


def education_prof_dev_category_view(request: HttpRequest) -> HttpResponse:
    prof_dev_courses = CategoryProfDev.objects.all().order_by('-rate')
    paginator = Paginator(prof_dev_courses, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'prof_dev_courses': prof_dev_courses,
        'page_obj': page_obj,
    }
    return render(request, 'education_templates/education_prof_dev.html', context=context)


def education_prof_dev_course_view(request: HttpRequest, category_slug) -> HttpResponse:
    category = get_object_or_404(CategoryProfDev, slug=category_slug)
    programs = ProgramProfDev.objects.select_related('category').filter(category=category)
    context = {'category': category, 'programs': programs}
    return render(request, 'education_templates/education_prof_dev_detail.html', context=context)
