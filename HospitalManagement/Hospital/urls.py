from django.contrib import admin
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('home/', home),
    path('error/', error_view),
    path('presidentLogin/', signin),
    path('presidentLogout/', signout),
    path('presidentIndex/', index),
    path('presidentDoctorView/', president_doctor_view),
    path('presidentStaffAdd/',president_staff_addition),
    path('presidentPatientView/', president_patient_view),
    path('presidentPatientAdd/',president_patient_addition),
    path('logoutStaff', logout_staff),
    path('doctorIndex/', doctor_index),
    path('receptionistIndex/', receptionist_index),
    path('receptionistPatientAddition/', receptionist_patient_addition, name="Patient Addition"),
    path('receptionistExistingPatient/', receptionist_existing_patient),
]