from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SideEffect(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=200, null=True)
    #json format string list
    side_effects = models.ManyToManyField(SideEffect, blank=True)
    side_effects_list = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now(), blank=True, null=True)
    #medications = models.ManyToManyField(CustomerMedication, blank=True)
    #json format string list
    my_side_effects_list = models.ManyToManyField(SideEffect, blank=True)

    def __str__(self):
        return self.user.username
class CustomerMedication(models.Model):
    medication = models.ForeignKey(Medication, null = True, on_delete=models.SET_NULL)
    treatment_for = models.CharField(max_length=200, null=True ,blank = True)
    dosage = models.CharField(max_length=200, null=True, blank = True)
    morning = models.BooleanField(default = False)
    midday = models.BooleanField(default = False)
    evening = models.BooleanField(default = False)
    bedtime = models.BooleanField(default = False)
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
    def __str__(self):
        if self.medication != None:
            return self.medication.name

class SymptomLog(models.Model):
    SEVERITY = (
        ('Mild', 'Mild'),
        ('Moderate', 'Moderate'),
        ('Severe', 'Severe'),
        ('Very Severe', 'Very Severe'),
        ('Worst Pain Possible', 'Worst Pain Possible')
    )
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
    side_effect = models.ForeignKey(SideEffect, null = True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    severity = models.CharField(max_length=200, choices = SEVERITY)
    duration_in_hours = models.FloatField(null=True)
    def __str__(self):
        name = "SYMPTOMLOG | Symptom: "+ self.side_effect.name+ "; Severity: "+ str(self.severity)+ "; Duration: "+ str(self.duration_in_hours)+"hour ; Date: "+ str(self.date_created)
        return name
class MedLog(models.Model):
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
    medication = models.ForeignKey(CustomerMedication, null = True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    number_of_doses = models.FloatField(null=True)
    def __str__(self):
        name = "Null"
        if self.medication != None:
            name = "MEDLOG | Medication: "+ self.medication.medication.name+ "; Doses: "+ str(self.number_of_doses)+ "; Date: "+ str(self.date_created)
        return name

class MedReminders(models.Model):
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
    medication = models.ForeignKey(Medication, null = True, on_delete=models.SET_NULL)
