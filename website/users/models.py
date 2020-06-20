from django.db import models

# Create your models here.
class SideEffect(models.Model):

    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Medication(models.Model):

    name = models.CharField(max_length=200, null=True)
    sideeffects = models.ManyToManyField(SideEffect)

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
