from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    """
    Users Login Form
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mt-5',
        'placeholder': 'Username',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mt-3',
        'placeholder': 'Password'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Password and Username is not matched")



class RegisterForm(UserCreationForm):
    """
    registration form
    """
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


