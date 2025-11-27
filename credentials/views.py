from django.shortcuts import render,redirect
from django.contrib.auth.models import User
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
    return render(request,"login.html")