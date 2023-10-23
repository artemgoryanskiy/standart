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
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView


from app_main.views import main_page_view, prof_train_search
from sitemap import (CategoryProfDevSitemap, CategoryProfRetrainSitemap, CategoryProfTrainSitemap,
                     EcoPassSitemap, EcoInvSitemap, EcoNmuSitemap, EcoPdvSitemap, EcoRegSitemap, EcoRepSitemap,
                     LabDocSitemap, LabOutSitemap, LabRiskSitemap, LabSoutSitemap,
                     ContactSitemap,
                     MainPageSitemap,)


sitemaps = {
    'cat_prof_dev': CategoryProfDevSitemap,
    'cat_prof_retr': CategoryProfRetrainSitemap,
    'cat_prof_train': CategoryProfTrainSitemap,

    'eco_pass': EcoPassSitemap,
    'eco_inv': EcoInvSitemap,
    'eco_nmu': EcoNmuSitemap,
    'eco_pdv': EcoPdvSitemap,
    'eco_reg': EcoRegSitemap,
    'eco_rep': EcoRepSitemap,

    'lab_doc': LabDocSitemap,
    'lab_out': LabOutSitemap,
    'lab_risk': LabRiskSitemap,
    'lab_sout': LabSoutSitemap,

    'contact': ContactSitemap,

    'main': MainPageSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view, name='main'),
    path('education-prof-dev/', include('app_prof_dev.urls')),
    path('education-prof-retr/', include('app_prof_retraining.urls')),
    path('education-prof-train/', include('app_prof_training.urls')),
    path('services/lab-prot/', include('app_lab_prot.urls')),
    path('services/ecology/', include('app_ecology.urls')),
    path('about-us/', include('app_about_us.urls')),
    path('news/', include('app_news.urls')),
    path('search/prof-train/', prof_train_search, name='prof_train_search'),
    path('tutors/', include('app_tutor.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
