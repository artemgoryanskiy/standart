from django.urls import path
from .views import get_about_edu_org_page


app_name = 'app_about_us'

urlpatterns = [
    path('edu-org/', get_about_edu_org_page, name='edu_org')
]