from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from user.form import SingUpForm

class SingUpView(CreateView):
    form_class = SingUpForm
    template_name = 'login/register.html'
    success_url = reverse_lazy('login')

# Create your views here.
def login(request):
    return HttpResponse("hola estas en el login")
