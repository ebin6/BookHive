from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method=="POST":
        first_name=request.POST['f_name']
        last_name=request.POST["last_name"]
        mail=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=mail).exists():
            return HttpResponse("User already exists")
        else:
            user=User.objects.create_user(username=mail,first_name=first_name,last_name=last_name,email=mail,password=password)
            user.save()
            return redirect("signin")
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        passwd=request.POST["password"]
        user=auth.authenticate(request,username=email,password=passwd)
        if user is not None:
            auth.login(request,user)
            return redirect("dashboard")
        else:
            return HttpResponse("Invalid username or password")
    return render(request,"login.html")