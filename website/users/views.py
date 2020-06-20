from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'users/dashboard.html')

def register(request):
    form = UserCreationForm();
    context = {'form':form}
    return render(request, 'users/register.html')
def login(request):
    context = {}
    return render(request, 'users/login.html')
def logs(request):
    return render(request, 'users/logs.html')
def medications(request):
    return render(request, 'users/medications.html')
def data(request):
    return render(request, 'users/data.html')
