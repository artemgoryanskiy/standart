from django.db.models import Q
from django.shortcuts import render
from app_prof_dev.models import CategoryProfDev, ProgramProfDev
from app_prof_retraining.models import CategoryProfRetrain, ProgramProfRetrain
from app_prof_training.models import CategoryProfTrain, ProgramProfTrain
from app_lab_prot.models import ProductLabProt
from app_ecology.models import ProductEco


def main_page_view(request):
    prof_dev_courses = CategoryProfDev.objects.all().filter(rate=4.5)[0:8]
    prof_retr_courses = CategoryProfRetrain.objects.all().filter(rate=4.5)[0:8]
    prof_train_courses = CategoryProfTrain.objects.all().filter(rate=4.5)[0:8]
    ot_services = ProductLabProt.objects.all().order_by('pk')
    eco_services = ProductEco.objects.all()
    context = {
        'prof_dev_courses': prof_dev_courses,
        'prof_retr_courses': prof_retr_courses,
        'prof_train_courses': prof_train_courses,
        'ot_services': ot_services,
        'eco_services': eco_services,
    }
    return render(request, 'index.html', context=context)


def prof_train_search(request):
    query = request.GET.get('query')
    programs_po = ProgramProfTrain.objects.filter(Q(title__icontains=query) | Q(code_num__icontains=query) |
                                                  Q(class_num__icontains=query))
    programs_pk = ProgramProfDev.objects.filter(Q(title__icontains=query))
    programs_pp = ProgramProfRetrain.objects.filter(Q(title__icontains=query) | Q(qualification__icontains=query))

    context = {'query': query, 'programs_po': programs_po, 'programs_pk': programs_pk, ' programs_pp':  programs_pp, }
    return render(request, 'search_templates/search_results.html', context=context)
