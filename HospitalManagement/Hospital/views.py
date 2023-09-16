from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import *
# Create your views here.


def signin(request):

    if (request.method=="POST"):
        username = request.POST['userName']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if (user is not None):
            
            login(request, user)
            return redirect('/presidentIndex')
        

        else:
            context = {"error": "Invalid username or password"}
            return render(request, 'President/president_login.html', context)


    return render(request, 'President/president_login.html')


def index(request):

    return render(request, 'President/president_index.html')

def president_doctor_view(request):
    staff = Staff.objects.all()
    return render(request, 'President/president_doctor_view.html',{'staff': staff})

def president_patient_view(request):
    return render(request, 'President/president_patient_view.html')

def president_patient_addition(request):
    
    return render(request,'President/president_patient_addition.html')

def president_staff_addition(request):
    roles = {
        'Doctor': 1,
        'Receptionist': 2
    }
    
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
        user.first_name = firstName+str(roles.get(role))
        user.last_name = lastName


        user.save()

        return render(request, 'President/president_doctor_view.html')
    
    
    return render(request, "President/president_staff_addition.html")


def home(request):
    if (request.method =='POST'):
        userName = request.POST['userName']
        password = request.POST['password']

        user = authenticate(username=userName, password=password)
        context = {"error": "Invalid username or password"}
        if 'doctor_form_signin' in request.POST:

            if (user is not None):
                if (user.first_name[-1]=='1'):
                    login(request, user)
                    return render(request,"Doctor/doctor_index.html")
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
                    return HttpResponse("<h1>Receptionist</h1>")
                else:
                    context = {"error": "Invalid role"}
                    messages.info(request, 'Invalid role!')
                    return render(request, "home.html", context)
            else:
                return render(request, "home.html", context)
            
    return render(request, "home.html")

            

def doctor_index(request):
    return render(request,"Doctor/doctor_index.html")
