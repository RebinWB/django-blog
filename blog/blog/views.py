from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic.edit import FormView, CreateView
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin


class RegisterView(UserPassesTestMixin, CreateView):
    """
    user registration view
    """
    template_name = "register.html"
    form_class = RegisterForm
    model = User

    def test_func(self):
        """
        prevent access of authenticated users
        """
        return not self.request.user.is_authenticated

    def form_valid(self, form):
        """
        if Register Form is valid, create new user with received values
        """
        user = form.save()  # register user
        login(self.request, user=user)  # login user after the registration
        return redirect("index")


class LoginView(UserPassesTestMixin, FormView):
    """
    Users Login View
    """
    template_name = 'login.html'
    form_class = LoginForm

    def test_func(self):
        """
        prevent access of authenticated users
        """
        return not self.request.user.is_authenticated

    def form_valid(self, form):
        """
        if form is valid, login user
        """
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(request=self.request, user=user)  # login user
            return redirect("index")

def logout_view(request):
    pass
