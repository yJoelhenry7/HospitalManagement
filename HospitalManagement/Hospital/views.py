from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.


def signin(request):

    if (request.user.is_authenticated and len(request.user.first_name)>0 and request.user.first_name[-1] not in ['1','2']):
        return redirect('/presidentIndex/')
    

    if (request.method=="POST"):
        username = request.POST['userName']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if (user is not None and len(user.first_name)>0 and user.first_name[-1] not in ['1','2']):
            
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
    if (request.method=='POST'):
        staff = Staff.objects.annotate().filter(name__icontains=request.POST['searchDoctor'])
    return render(request, 'President/president_doctor_view.html',{'staff': staff})

def president_patient_view(request):
    patients = Patient.objects.all()
    if (request.method=='POST'):
        patients = Patient.objects.annotate().filter(name__icontains=request.POST['searchPatient'])
    return render(request, 'President/president_patient_view.html', {'patients': patients})

def president_patient_addition(request):
    
    return render(request,'President/president_patient_addition.html')

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
                city = city,
                role = role
            )
        staff.save()
        
        user = User.objects.create_user(userName, email, password)
        if (role=='Receptionist'):
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
    if (request.user.is_authenticated and len(request.user.first_name)>0):
        if (request.user.first_name[-1]=='1'):
            return redirect('/doctorIndex/')
        elif (request.user.first_name[-1]=='2'):
            return redirect('/receptionistIndex/')
        else:
            logout(request)
    if (request.method =='POST'):
        userName = request.POST['userName']
        password = request.POST['password']

        user = authenticate(username=userName, password=password)
        context = {"error": "Invalid username or password"}
        if 'doctor_form_signin' in request.POST:

            if (user is not None and len(user.first_name)>0):
                if (user.first_name[-1]=='1'):
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
                if (user.first_name[-1]=='2'):
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
    if (request.user.is_authenticated):
        if (len(request.user.first_name)>0 and request.user.first_name[-1]=='1'):
            return render(request,"Doctor/doctor_index.html")
        else:
            logout(request)
            return redirect('/home/')
    logout(request)
    return redirect('/home/')
    

def receptionist_index(request):
    return render(request, "Receptionist/receptionist_index.html")

def receptionist_patient_addition(request):
    return render(request, "Receptionist/receptionist_patient_addition.html")

def receptionist_existing_patient(request):
    return render(request, "Receptionist/receptionist_existing_patient.html")
