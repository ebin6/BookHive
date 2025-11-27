from django.shortcuts import render

# Create your views here.

def register(request):
    if request.method=="POST":
        first_name=request.POST['f_name']
        last_name=request.POST["last_name"]
        mail=request.POST['email']
        password=request.POST['password']
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")