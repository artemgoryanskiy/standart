from django.urls import path
from .views import CategoryListView, program_list


app_name = 'app_prof_training'

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('<slug:category_slug>/', program_list, name='program_list'),

]