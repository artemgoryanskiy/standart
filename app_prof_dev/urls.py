from django.urls import path
from app_prof_dev.views import education_prof_dev_category_view, education_prof_dev_course_view

app_name = 'app_prof_dev'


urlpatterns = [
    path('', education_prof_dev_category_view, name='education_prof_dev'),
    path('<slug:category_slug>/', education_prof_dev_course_view, name='prof_dev_course'),
]
