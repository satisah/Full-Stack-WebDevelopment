from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def homepage(request):
    return render(request,'FirstUserInter.html')
def RoadMap(request):
    return render(request,'RoadMap.html')
def frontend(request):
    return render(request,'Front end.html')
def Backend(request):
    return render(request,'Back end.html')
def Database(request):
    return render(request,'Database.html')
def About(request):
    return render(request,'About.html')
def Contact(request):
    return render(request,'Contact.html')






def registerpage(request):
    form=UserCreationForm() #create a blank user creation form
    if request.method=='POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html',{'form':form})

def loginpage(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        user=authenticate(request,username=uname,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('FirstUserInter')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')
