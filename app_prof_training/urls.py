from django.urls import path

from .views import education_prof_train_category_view, education_prof_train_course_view


app_name = 'app_prof_training'


urlpatterns = [
    path('', education_prof_train_category_view, name='education_prof_train'),
    path('<slug:category_slug>/', education_prof_train_course_view, name='prof_train_course'),
]
