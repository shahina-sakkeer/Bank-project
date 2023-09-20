from django.shortcuts import redirect, render
from django.contrib import auth
from bankapp.forms import ApplicationForm


# Create your views here.

def demo(request):
    return render(request,"index.html")

def form_view(request):
    message = None
    if request.method == 'POST':
        print("submitted")
        message = "Your application has been accepted!!!"
    return render(request,"home.html",{"message":message})   


def newdemo(request):
    return render(request,"demo.html")  

def logout(request):
    auth.logout(request)
    return redirect('bankapp:home')  
