from django import forms


class BannerSearchForm(forms.Form):
    query = forms.CharField(label='Искать курс', max_length=100)
