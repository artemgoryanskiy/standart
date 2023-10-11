from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import render

from .forms import ContactForm
from .models import Document


def contact_us_view(request: HttpRequest):
    sent = False
    documents = Document.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Новое сообщение от {first_name}, email {email}',
                message,
                'info@standart82.ru',
                ['info@standart82.ru'],
                fail_silently=False,
            )
            sent = True
    else:
        form = ContactForm()
    context = {
        'form': form,
        'sent': sent,
        'documents': documents,
    }
    return render(request, 'about_templates/contacts.html', context=context)
