from django.urls import path
from .views import CategoryListView, program_list, main_study_page_view


app_name = 'app_prof_dev'


urlpatterns = [
    path('', main_study_page_view, name='main_study'),
    path('professional-development/', CategoryListView.as_view(), name='category_list'),
    path('professional-development/<slug:category_slug>/', program_list, name='program_list'),
]