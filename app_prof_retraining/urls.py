from django.urls import path
from .views import education_prof_retr_category_view, education_prof_retr_course_view


app_name = 'app_prof_retraining'


urlpatterns = [
    path('', education_prof_retr_category_view, name='education_prof_retr'),
    path('<slug:category_slug>/', education_prof_retr_course_view, name='prof_retr_course'),
]
