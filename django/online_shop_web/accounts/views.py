from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views

from . import forms


class SignUp(generic.CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super(SignUp, self).get(request, *args, **kwargs)


class Login(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super(Login, self).get(request, *args, **kwargs)



