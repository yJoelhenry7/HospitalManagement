from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField('Doctor Name', max_length=100)
    firstName = models.CharField('First Name', max_length=50)
    lastName = models.CharField('last Name', max_length=50)
    email = models.EmailField('Email', max_length=100)
    mobileNumber = models.CharField('Mobile Number', max_length=15)
    aadharNumber = models.CharField('Aadhar Number', max_length=15)
    city = models.CharField('City', max_length=50)

class Staff(models.Model):
    name = models.CharField('Doctor Name', max_length=100)
    firstName = models.CharField('First Name', max_length=50)
    lastName = models.CharField('last Name', max_length=50)
    email = models.EmailField('Email', max_length=100)
    mobileNumber = models.CharField('Mobile Number', max_length=15)
    aadharNumber = models.CharField('Aadhar Number', max_length=15)
    city = models.CharField('City', max_length=50)
    role = models.CharField('Role', max_length=15)
