from django.db import models
from datetime import date
# Create your models here.

class Patient(models.Model):
    name = models.CharField('Doctor Name', max_length=100)
    firstName = models.CharField('First Name', max_length=50)
    lastName = models.CharField('last Name', max_length=50)
    dateOfBirth = models.DateField(default=date.today())
    gender = models.CharField('Gender', max_length=50, default='Male')
    email = models.EmailField('Email', max_length=100, null=True)
    mobileNumber = models.CharField('Mobile Number', max_length=15)
    aadharNumber = models.CharField('Aadhar Number', max_length=15)
    city = models.CharField('City', max_length=50)
    symptoms = models.CharField('Symptoms',max_length=100,default="None")
    diagnosis = models.CharField('Diagnosis', max_length=100,default="None")
    prescription = models.CharField('Prescription', max_length=100,default="None")

class visits(models.Model):
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dateOfRegistration = models.DateField()
    symptoms = models.CharField('Symptoms', max_length=100)
    diagnosis = models.CharField('Diagnosis', max_length=100)
    prescription = models.CharField('Prescription', max_length=100)

class applications(models.Model):
    visit = models.ForeignKey(visits, on_delete=models.CASCADE)
    

class Staff(models.Model):
    name = models.CharField('Doctor Name', max_length=100)
    firstName = models.CharField('First Name', max_length=50)
    lastName = models.CharField('last Name', max_length=50)
    email = models.EmailField('Email', max_length=100, null=True)
    mobileNumber = models.CharField('Mobile Number', max_length=15)
    aadharNumber = models.CharField('Aadhar Number', max_length=15)
    city = models.CharField('City', max_length=50)
    role = models.CharField('Role', max_length=15)
