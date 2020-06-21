from django.db import models

# Create your models here.
class SideEffect(models.Model):

    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Medication(models.Model):

    name = models.CharField(max_length=200, null=True)
    treatment_for = models.CharField(max_length=200, null=True)
    side_effects = models.ManyToManyField(SideEffect)
    dosage = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    medications = models.ManyToManyField(Medication)

    def __str__(self):
        return self.name
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
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    severity = models.CharField(max_length=200, choices = SEVERITY)
    durarion_in_hours = models.FloatField(null=True)
class MedLog(models.Model):
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
    medication = models.ForeignKey(Medication, null = True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    number_of_doses = models.FloatField(null=True)
    def __str__(self):
        name = "MEDLOG | Medication: "+ self.medication.name+ "; Doses: "+ str(self.number_of_doses)+ "; Date: "+ str(self.date_created)
        return name
