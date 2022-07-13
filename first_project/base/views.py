from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView


class Customlogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'


