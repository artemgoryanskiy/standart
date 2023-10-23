from django import forms
from .models import BecomeTutor
from django.forms import TextInput


class TutorForm(forms.ModelForm):
    class Meta:
        model = BecomeTutor
        fields = ['last_name', 'first_name', 'patronymic', 'education', 'work_experience', 'phone', 'email',]
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'patronymic': 'Отчество',
            'education': 'Наименование учебного заведения и год окончания',
            'work_experience': 'Стаж работы (лет)',
            'phone': 'Телефон',
        }
        widgets = {
            'phone': TextInput(attrs={'data-mask': 'phone'}),
        }
