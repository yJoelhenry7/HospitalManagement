from django.contrib import admin
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('presidentLogin/', signin),
    path('presidentIndex/', index),
    path('presidentDoctorView/', president_doctor_view),
    path('presidentStaffAdd/',president_staff_addition),
    path('doctorIndex/', doctor_index),
    path('presidentPatientView/', president_patient_view),
    path('presidentPatientAdd/',president_patient_addition),
]