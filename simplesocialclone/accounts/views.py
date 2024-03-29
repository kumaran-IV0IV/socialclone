from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.views.generic import CreateView
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreate
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'