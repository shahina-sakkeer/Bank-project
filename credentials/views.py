from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.urls import reverse
# Create your views here.

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        cpassword=request.POST["confirm_password"]

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is already taken !!!")
                return redirect('credentials:signup')
            
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                messages.info(request,"registration completed !!!")
                print("user created")    
        else:
            messages.info(request,"password incorrect !!!")
            return redirect('credentials:signup')

        return redirect('credentials:signin')   


    return render(request,"register.html")


def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('bankapp:application')
        else:
            messages.info(request,"invalid username !!!")
            return redirect('credentials:signin')
    return render(request,"login.html")    


