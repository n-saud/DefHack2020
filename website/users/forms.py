from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class MedlogForm(ModelForm):
    class Meta:
        model = MedLog
        fields = '__all__'
class MedicationForm(ModelForm):
    class Meta:
        model = Medication
        fields = '__all__'
class SymptomLogForm(ModelForm):
    class Meta:
        model = SymptomLog
        fields = '__all__'
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
