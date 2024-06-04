from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': _('Nazwa użytkownika'),
            'email': _('Adres e-mail'),
            'password1': _('Hasło'),
            'password2': _('Potwierdź hasło'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = _('Nazwa użytkownika')
        self.fields['email'].label = _('Adres e-mail')
        self.fields['password1'].label = _('Hasło')
        self.fields['password2'].label = _('Potwierdź hasło')
        # Usuwanie help_text
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8 or password1.isdigit():
            raise ValidationError([
                _('Twoje hasło nie może być zbyt podobne do twoich innych danych osobistych.'),
                _('Twoje hasło musi zawierać co najmniej 8 znaków.'),
                _('Twoje hasło nie może być powszechnie używanym hasłem.'),
                _('Twoje hasło nie może składać się tylko z cyfr.')
            ])
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError(_('Hasła się nie zgadzają.'))
        return password2

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(), label=_('Nazwa użytkownika'))
    password = forms.CharField(widget=PasswordInput(), label=_('Hasło'))
