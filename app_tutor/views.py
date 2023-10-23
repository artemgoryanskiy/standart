from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View

from app_tutor.models import Tutor
from .forms import TutorForm


class BecomeTutorView(View):
    def get(self, request, *args, **kwargs):
        tutors = Tutor.objects.all()
        form = TutorForm()
        context = {'tutors': tutors,'form': form}
        return render(request, 'tutor_templates/tutor_list.html', context)

    def post(self, request, *args, **kwargs):
        tutors = Tutor.objects.all()
        form = TutorForm(data=request.POST)
        sent = False

        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            send_mail(
                f'Новое сообщение от {first_name}, email {email}',
                'Заявка на педагога',
                'info@standart82.ru',
                ['info@standart82.ru'],
                fail_silently=False,
            )
            sent = True
            form = TutorForm()
            return render(request, 'tutor_templates/tutor_list.html', {'tutors': tutors, 'form': form})
        return render(request, 'tutor_templates/tutor_list.html', {'tutors': tutors, 'form': form})
