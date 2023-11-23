from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, Textarea ,TextInput
from django import forms



# - Register/Create User 

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1','password2']


# - Login User

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

