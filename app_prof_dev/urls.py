from django.urls import path
from .views import CategoryListView, program_list


app_name = 'app_prof_dev'


urlpatterns = [
    path('prof-devel/', CategoryListView.as_view(), name='category_list'),
    path('prof-devel/<slug:category_slug>/', program_list, name='program_list'),
]