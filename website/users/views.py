from django.shortcuts import render, redirect
from django.http import HttpResponse

from.models import *

def home(request):
    medications = Medication.objects.all() #change later
    medications_count = medications.count()
    side_effects_count =0
    for med in medications:
        side_effects_count = side_effects_count + med.side_effects.count()
    logs = MedLog.objects.all() #change later
    symptomlogs_count = SymptomLog.objects.all().count() #change later
    medlogs_count = MedLog.objects.all().count() #change later
    context = {'medications_count': medications_count, 'side_effects_count': side_effects_count,
    'symptomlogs_count': symptomlogs_count, 'medlogs_count': medlogs_count, 'medications': medications, 'logs': logs}
    return render(request, 'users/dashboard.html',context)

def register(request):
    form = UserCreationForm();
    context = {'form':form}
    return render(request, 'users/register.html')
def login(request):
    context = {}
    return render(request, 'users/login.html')
def medlogs(request):
    logs = MedLog.objects.all() #change later
    return render(request, 'users/logs.html',{'logs':logs})
def symptomlogs(request):
    logs = SymptomLog.objects.all() #change later
    return render(request, 'users/logs.html',{'logs':logs})
def medications(request):
    medications = Medication.objects.all() #change later
    return render(request, 'users/medications.html',{'medications':medications})
def data(request):
    return render(request, 'users/data.html')
