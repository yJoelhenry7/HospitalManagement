# Generated by Django 4.1.7 on 2023-09-20 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0008_visits_applications'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(default='cold', max_length=100, verbose_name='Symptoms'),
        ),
    ]
