from django.urls import path
from .views import BecomeTutorView


app_name = 'app_tutor'


urlpatterns = [
    path('', BecomeTutorView.as_view(), name='tutor_list'),
    # path('become/', BecomeTutorView.as_view(), name='become_tutor'),
]