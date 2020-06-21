from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(SideEffect)
admin.site.register(Medication)
admin.site.register(SymptomLog)
admin.site.register(MedLog)
admin.site.register(Time)
