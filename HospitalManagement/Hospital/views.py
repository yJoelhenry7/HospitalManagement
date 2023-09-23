from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from .models import *
# Create your views here.


def signin(request):

    if (request.user.is_authenticated and len(request.user.first_name) > 0 and request.user.first_name[-1] not in ['1', '2']):
        return redirect('/presidentIndex/')

    if (request.method == "POST"):
        username = request.POST['userName']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if (user is not None and len(user.first_name) > 0 and user.first_name[-1] not in ['1', '2']):

            login(request, user)
            return redirect('/presidentIndex')

        else:
            context = {"error": "Invalid username or password"}
            return render(request, 'President/president_login.html', context)

    return render(request, 'President/president_login.html')


def signout(request):
    logout(request)
    return redirect('/presidentLogin/')


def index(request):

    return render(request, 'President/president_index.html')


def president_doctor_view(request):
    staff = Staff.objects.all()
    if (request.method == 'POST'):
        staff = Staff.objects.annotate().filter(
            name__icontains=request.POST['searchDoctor'])
    return render(request, 'President/president_doctor_view.html', {'staff': staff})


def president_patient_view(request):
    patients = Patient.objects.all()
    if (request.method == 'POST'):
        patients = Patient.objects.annotate().filter(
            name__icontains=request.POST['searchPatient'])
    return render(request, 'President/president_patient_view.html', {'patients': patients})


def president_staff_addition(request):

    if (request.method == "POST"):
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        mobilenumber = request.POST['mobileNumber']
        aadharnumber = request.POST['aadharNumber']
        city = request.POST['city']
        role = request.POST['role']
        password = aadharnumber[:4]+mobilenumber[-4:]
        userName = lastName+aadharnumber[:2]+mobilenumber[-2:]

        staff = Staff(
            name=(firstName+" "+lastName),
            firstName=(firstName),
            lastName=(lastName),
            email=email,
            mobileNumber=mobilenumber,
            aadharNumber=aadharnumber,
            city=city,
            role=role
        )
        staff.save()

        user = User.objects.create_user(userName, email, password)
        if (role == 'Receptionist'):
            en = '2'
        else:
            en = '1'
        user.first_name = firstName+en
        user.last_name = lastName

        user.save()

        return render(request, 'President/president_doctor_view.html')

    return render(request, "President/president_staff_addition.html")


def emptyUrl(request):
    return redirect('/home/')


def error_view(request):
    return render(request, 'Error/error.html', status=404)


def logout_staff(request):
    logout(request)
    return redirect('/home/')


def home(request):
    if (request.user.is_authenticated and len(request.user.first_name) > 0):
        if (request.user.first_name[-1] == '1'):
            return redirect('/doctorIndex/')
        elif (request.user.first_name[-1] == '2'):
            return redirect('/receptionistIndex/')
        else:
            logout(request)
    if (request.method == 'POST'):
        userName = request.POST['userName']
        password = request.POST['password']

        user = authenticate(username=userName, password=password)
        context = {"error": "Invalid username or password"}
        if 'doctor_form_signin' in request.POST:

            if (user is not None and len(user.first_name) > 0):
                if (user.first_name[-1] == '1'):
                    login(request, user)
                    return redirect('/doctorIndex/')
                else:
                    context = {"error": "Invalid role"}
                    messages.info(request, 'Invalid role!')
                    return render(request, "home.html", context)
            else:
                return render(request, "home.html", context)
        elif 'receptionist_form_signin' in request.POST:

            if (user is not None):
                if (user.first_name[-1] == '2'):
                    login(request, user)
                    return redirect('/receptionistIndex/')
                else:
                    context = {"error": "Invalid role"}
                    messages.info(request, 'Invalid role!')
                    return render(request, "home.html", context)
            else:
                return render(request, "home.html", context)

    return render(request, "home.html")


def doctor_index(request):
    error = " "
    # visits.objects.all().delete()
    # Patient.objects.all().delete()
    
    if (request.user.is_authenticated):
        if (len(request.user.first_name) > 0 and request.user.first_name[-1] == '1'):

            if (request.method == 'POST'):
                pid = request.POST['application_id']
                visit1 = visits.objects.filter(patientId=pid).first()
                if visit1 == None:
                    application = applications.objects.all()
                    error = "No data Matched"
                    return render(request, 'Doctor/doctor_index.html', {'person': application, "error": error, "app_id": pid, "visit2": application})
                else:
                    error = ""
                    visit2 = visits.objects.filter(patientId=pid).first()
                    visit1 = Patient.objects.filter(id=pid).first()
                    return render(request, 'Doctor/doctor_index.html', {'person': visit1, "error": error, "app_id": pid, "visit2": visit2})

        else:
            logout(request)
            return redirect('/home/')

    application = applications.objects.all()
    return render(request, "Doctor/doctor_index.html", {'person': application, "error": error, "visit2": application})


def review_patient(request):
    error = " "
    if (request.method == 'POST'):
        pid = request.POST['patientid']
        symptoms = request.POST['symptoms']
        diagnosis = request.POST['diagnosis']
        prescription = request.POST['prescription']
        dateOfRegistration = date.today()
        visit1 = visits.objects.filter(patientId=pid).first()
        if visit1 == None:
            application = applications.objects.all()
            return redirect("doctor_index")
        else:
            Patient.objects.filter(id=pid).update(symptoms=symptoms)
            Patient.objects.filter(id=pid).update(diagnosis=diagnosis)
            Patient.objects.filter(id=pid).update(prescription=prescription)
            return redirect('doctor_index')

    return redirect('doctor_index')


def receptionist_index(request):
    pid=0
    application = applications.objects.all()
    if (request.method == 'POST'):
        pid = request.POST['searchDoctor']
        visit1 = visits.objects.filter(patientId=pid).first()
        visit = applications.objects.filter(visit=visit1).all()
        if (visit1 == None ):
            return render(request, "Receptionist/receptionist_index.html", {'application': application,'pid':pid})

        else:
            return render(request, "Receptionist/receptionist_index.html", {'application': visit,'pid':pid})

    
    return render(request, "Receptionist/receptionist_index.html", {'application': application,'pid':pid})


def receptionist_patient_addition(request):
    error=""
    if (request.method == 'POST'):
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        dateOfBirth = request.POST['date_of_birth']
        gender = request.POST['gender']
        email = request.POST['email']
        mobilenumber = request.POST['mobileNumber']
        aadharnumber = request.POST['aadharNumber']
        city = request.POST['city']
        visit1 = Patient.objects.filter(mobileNumber=mobilenumber).first()
        if visit1 != None:
            error="User Already Exists\n"
            return render(request, "Receptionist/receptionist_patient_addition.html",{"error":error})
        patient = Patient(
            name=(firstName+" "+lastName),
            firstName=(firstName),
            lastName=(lastName),
            dateOfBirth=dateOfBirth,
            gender=gender,
            email=email,
            mobileNumber=mobilenumber,
            aadharNumber=aadharnumber,
            city=city
        )
        patient.save()
        visit = visits(patientId=patient, dateOfRegistration=date.today())
        visit.save()
        return redirect('new_user', patient_id=patient.id)

    return render(request, "Receptionist/receptionist_patient_addition.html",{"error":error})


def new_user(request, patient_id):
    error = " "
    if (request.method == 'POST'):
        pid = patient_id
        visit = Patient.objects.filter(id=pid).first()
        if (visit == None):
            return HttpResponse("No person found with that ID")
        symptoms = request.POST['symptoms']
        visit1 = visits.objects.filter(patientId=pid).first()
        if visit1 == None:
            error = "Id doesn't exist"

            return render(request, "Receptionist/receptionist_index.html", {'error': error})
        else:
            Patient.objects.filter(id=pid).update(symptoms=symptoms)
            visits.objects.filter(patientId=pid).update(symptoms=symptoms)
            application = applications(visit=visit1)
            application.save()
            return redirect('Receptionist Index')
    else:
        return render(request, "Receptionist/receptionist_existing_patient.html", {'error': error})


def receptionist_existing_patient(request, patient_id):
    error = " "
    if (request.method == 'POST'):
        pid = patient_id
        visit = Patient.objects.filter(id=pid).first()

        if (visit == None):
            return HttpResponse("No person found with that ID")
        symptoms = request.POST['symptoms']
        visit1 = visits.objects.filter(patientId=pid).first()
        if visit1 == None:
            error = "Id doesn't exist"

            return render(request, "Receptionist/receptionist_index.html", {'error': error})
        else:
            visits.objects.filter(patientId=pid).update(symptoms=symptoms)  

            return redirect('Receptionist Index')
    else:
        return render(request, "Receptionist/receptionist_existing_patient.html", {'error': error})
