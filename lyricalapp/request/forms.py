from django import forms
from .models import Request
from django.utils.translation import gettext_lazy as _

class RequestForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ['song_name', 'author']
        labels = {'song_name': _('Nazwa piosenki'), 'author': _('Autor')}