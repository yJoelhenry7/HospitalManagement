# Generated by Django 4.1.7 on 2023-09-20 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0007_rename_date_of_birth_patient_dateofbirth_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='visits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfRegistration', models.DateField()),
                ('symptoms', models.CharField(max_length=100, verbose_name='Symptoms')),
                ('diagnosis', models.CharField(max_length=100, verbose_name='Diagnosis')),
                ('prescription', models.CharField(max_length=100, verbose_name='Prescription')),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.visits')),
            ],
        ),
    ]
