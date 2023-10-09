from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView

from app_prof_dev.models import CategoryProfDev, ProgramProfDev
from app_prof_retraining.models import CategoryProfRetrain, ProgramProfRetrain
from app_prof_training.models import CategoryProfTrain, ProgramProfTrain
from app_lab_prot.models import ProductLabProt
from app_ecology.models import ProductEco
from app_about_us.models import Contact, Document
from app_about_us.forms import ContactForm
from app_news.models import CategoryNews, PostNews
from app_news.forms import CommentForm

from app_prof_training.forms import BannerSearchForm
from itertools import chain


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


def education_prof_dev_category_view(request):
    prof_dev_courses = CategoryProfDev.objects.all().order_by('-rate')
    paginator = Paginator(prof_dev_courses, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'prof_dev_courses': prof_dev_courses,
        'page_obj': page_obj,
    }
    return render(request, 'education_templates/education_prof_dev.html', context=context)


def education_prof_dev_course_view(request, category_slug):
    category = get_object_or_404(CategoryProfDev, slug=category_slug)
    programs = ProgramProfDev.objects.select_related('category').filter(category=category)
    context = {'category': category, 'programs': programs}
    return render(request, 'education_templates/education_prof_dev_detail.html', context=context)


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
    return render(request, 'education_templates/education_prof_retr_detail.html', context=context)


def lab_prot_view(request, slug):
    if slug == 'specialnaya-ocenka-uslovij-truda-sout':
        return render(request, 'services_templates/lab_prot/lab_prot_spec.html', context={})
    elif slug == 'ocenka-professionalnyh-riskov':
        return render(request, 'services_templates/lab_prot/lab_prot_risks.html', context={})
    elif slug == 'razrabotka-komplekta-dokumentov-po-ohrane-truda':
        return render(request, 'services_templates/lab_prot/lab_prot_doc.html', context={})
    elif slug == 'autsorsing-po-ohrane-truda':
        return render(request, 'services_templates/lab_prot/lab_prot_outsourcing.html', context={})


def ecology_view(request, slug):
    if slug == 'pasporta-othodov':
        return render(request, 'services_templates/ecology/ecology_eco_pass.html', context={})
    elif slug == 'inventarizaciya-istochnikov-i-vybrosov-zagryaznyayushih-veshestv-v-atmosfernyj-vozduh':
        return render(request, 'services_templates/ecology/ecology_inventory.html', context={})
    elif slug == 'postanovka-na-uchet-obektov-negativnogo-vozdejstviya-na-okruzhayushuyu-sredu-nvos':
        return render(request, 'services_templates/ecology/ecology_registration.html', context={})
    elif slug == 'meropriyatiya-po-umensheniyu-vybrosov-zagryaznyayushih-veshestv-v-atmosfernyj-vozduh-v-periody-neblagopriyatnyh-meteorologicheskih-uslovij-nmu':
        return render(request, 'services_templates/ecology/ecology_nmu.html', context={})
    elif slug == 'proekt-predelno-dopustimyh-vybrosov-v-atmosferu-proekt-pdv':
        return render(request, 'services_templates/ecology/ecology_project.html', context={})
    elif slug == 'ekologicheskaya-otchetnost':
        return render(request, 'services_templates/ecology/ecology_report.html', context={})


def prof_train_search(request):
    query = request.GET.get('query')
    programs_po = ProgramProfTrain.objects.filter(Q(title__icontains=query) | Q(code_num__icontains=query) | Q(class_num__icontains=query))
    programs_pk = ProgramProfDev.objects.filter(Q(title__icontains=query))
    programs_pp = ProgramProfRetrain.objects.filter(Q(title__icontains=query) | Q(qualification__icontains=query))

    context = {'query': query, 'programs_po': programs_po, 'programs_pk': programs_pk, ' programs_pp':  programs_pp,}
    return render(request, 'search_templates/search_results.html', context=context)


def contact_us_view(request: HttpRequest):
    sent = False
    documents = Document.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Новое сообщение от {first_name}, email {email}',
                message,
                'info@standart82.ru',
                ['info@standart82.ru'],
                fail_silently=False,
            )
            sent = True
    else:
        form = ContactForm()
    context = {
        'form': form,
        'sent': sent,
        'documents': documents,
    }
    return render(request, 'about_templates/contacts.html', context=context)


def news_list_view(request):
    news = PostNews.objects.all().select_related('category')
    paginator = Paginator(news, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news_templates/news_grid.html', context={'news': news, 'page_obj': page_obj,})


def news_detail_view(request: HttpRequest, slug) -> HttpResponse:
    post = get_object_or_404(PostNews, slug=slug)
    comments = post.comments.all()
    new_comment = False
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'news_templates/news_detail.html', context=context)


# class NewsDetailView(DetailView):
#     model = PostNews
#     context_object_name = 'post'
#     template_name = 'news_templates/news_detail.html'