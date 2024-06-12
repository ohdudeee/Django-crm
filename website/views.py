from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    # if user logging in
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have logged IN!")
            return redirect('home') 
        else:
            messages.success(request,"There is some error..try again....")
            return redirect('home')
    else:
       return render(request,'home.html',{})


def login_user(request):
    pass

def logout_user(request):
    pass