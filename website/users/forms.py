from django.forms import ModelForm
from .models import *

class MedlogForm(ModelForm):
    class Meta:
        model = MedLog
        fields = '__all__'
