from django.urls import path

from .views import contact_us_view


app_name = 'app_about_us'


urlpatterns = [
    path('contacts/', contact_us_view, name='contacts'),
]