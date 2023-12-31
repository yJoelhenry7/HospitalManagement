# Generated by Django 4.0.1 on 2023-09-21 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0009_patient_symptoms'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='diagnosis',
            field=models.CharField(default='None', max_length=100, verbose_name='Diagnosis'),
        ),
        migrations.AddField(
            model_name='patient',
            name='prescription',
            field=models.CharField(default='None', max_length=100, verbose_name='Prescription'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dateOfBirth',
            field=models.DateField(default=datetime.date(2023, 9, 21)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(default='fhkef', max_length=100, verbose_name='Symptoms'),
        ),
    ]
