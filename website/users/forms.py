from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('name','phone','email','profile_pic')
class MedlogForm(ModelForm):
    class Meta:
        model = MedLog
        fields = '__all__'
        exclude  = ('customer',)
    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('customer', None)
        super(MedlogForm, self).__init__(*args, **kwargs)
        if customer != None:
            self.fields['medication'].queryset = customer.customermedication_set.all()

class SideEffectForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('my_side_effects_list',)
class MedicationForm(ModelForm):
    class Meta:
        model = CustomerMedication
        exclude = ('customer',)
class UpdateMedicationForm(ModelForm):
    class Meta:
        model = CustomerMedication
        exclude = ('medication',)
class SymptomLogForm(ModelForm):
    class Meta:
        model = SymptomLog
        fields = '__all__'
        exclude  = ('customer',)
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
