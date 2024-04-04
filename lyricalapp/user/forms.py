from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput


# tworzymy formularz do tworzenia użytkownika przy wykorzystaniu wbudowanego formularza django
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        # password1 = hasło użytkownika, password2 jest używane do pola "potwierdz haslo"
        fields = ['username', 'email', 'password1', 'password2']


# tworzymy formularz do logowania przy wykorzystaniu wbudowanego formularza django

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())