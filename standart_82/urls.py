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
from app_prof_dev.views import main_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view, name='main'),
    path('study/', include('app_prof_dev.urls')),
    # path('professional-development/', include('app_prof_dev.urls')),
    path('study/professional-retraining/', include('app_prof_retraining.urls')),
    path('study/professional-training/', include('app_prof_training.urls')),
    path('news/', include('app_news.urls')),
    path('ecology/', include('app_ecology.urls')),
    path('labor-protection/', include('app_lab_prot.urls')),
    path('about-us/', include('app_about_us.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)