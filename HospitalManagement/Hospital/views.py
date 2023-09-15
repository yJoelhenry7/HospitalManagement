from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
    return render(request, 'President/president_doctor_view.html')

def president_patient_view(request):
    return render(request, 'President/president_patient_view.html')

def president_patient_addition(request):
    
    return render(request,'President/president_patient_addition.html')

def president_doctor_addition(request):
    
    if (request.method == "POST"):
        userName = request.POST['userName']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        mobilenumber = request.POST['mobileNumber']
        aadharnumber = request.POST['aadharNumber']
        city = request.POST['city']
        password = aadharnumber[:4]+mobilenumber[-4:]
       

        user = User.objects.create_user(userName, email, password)
        user.first_name = firstName
        user.last_name = lastName



        user.save()

        return render(request, 'President/president_doctor_view.html', {'firstName': firstName})
    
    
    return render(request, "President/president_doctor_addition.html")

def home(request):

    return HttpResponse("This is home page")