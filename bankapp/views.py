from django.shortcuts import redirect, render
from django.contrib import auth,messages
from .forms import ApplicationForm

# Create your views here.

def demo(request):
    return render(request,"index.html")

def form_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Application Accepted !!!')
            return redirect('bankapp:forms')
    else:
        form = ApplicationForm()
    return render(request, 'home.html', {'form': form})


def newdemo(request):
    return render(request,"demo.html")  

def logout(request):
    auth.logout(request)
    return redirect('bankapp:home')  
