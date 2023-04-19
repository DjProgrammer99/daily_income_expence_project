from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return render(request,'home.html')

def adduser(request):
    if request.method=='POST':
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserCreationForm()
        context = {'form':f}
        return render(request,'adduser.html',context)
from .models import LoginForm

from django.contrib.auth import login,logout,authenticate

def login_view(request):
    if request.method=='POST':
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        
        user = authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['uid'] = user.id
            login(request,user)
       
            return redirect('/')
        else:
            f= LoginForm
            context = {'form':f}
            return render(request,'login.html',context)
    else:
        f= LoginForm
        context = {'form':f}
        return render(request,'login.html',context)
    
def logout_view(request):
    logout(request)
    return redirect("/")
    