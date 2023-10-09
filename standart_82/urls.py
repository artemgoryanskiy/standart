"""standart_82 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
# from app_prof_dev.views import main_page_view
from app_main.views import (
    main_page_view,
    education_prof_dev_category_view, education_prof_retr_category_view, education_prof_dev_course_view,
    education_prof_retr_course_view, education_prof_train_category_view, education_prof_train_course_view,
    lab_prot_view,
    ecology_view,
    prof_train_search,
    contact_us_view,
    news_list_view,
    news_detail_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view, name='main'),
    path('education-prof-dev/', education_prof_dev_category_view, name='education_prof_dev'),
    path('education-prof-dev/<slug:category_slug>/', education_prof_dev_course_view, name='prof_dev_course'),
    path('education-prof-retr/', education_prof_retr_category_view, name='education_prof_retr'),
    path('education-prof-retr/<slug:category_slug>/', education_prof_retr_course_view, name='prof_retr_course'),
    path('education-prof-train/',education_prof_train_category_view, name='education_prof_train'),
    path('education-prof-train/<slug:category_slug>/', education_prof_train_course_view, name='prof_train_course'),

    path('services/lab-prot/<slug:slug>/', cache_page(60*24)(lab_prot_view), name='lab_prot'),

    path('services/ecology/<slug:slug>/', cache_page(60*24)(ecology_view), name='ecology'),
    path('about-us/contacts/', contact_us_view, name='contacts'),

    path('news/', news_list_view, name='news'),
    path('news/<slug:slug>/', news_detail_view, name='news_detail'),

    path('ecology/', include('app_ecology.urls')),
    path('labor-protection/', include('app_lab_prot.urls')),


    path('search/prof-train/', prof_train_search, name='prof_train_search'),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)