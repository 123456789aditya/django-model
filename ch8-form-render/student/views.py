from django.shortcuts import render

# Create your views here.
from student.forms import Registration,Login

def Final(request):
    sea=Registration()
    return render(request,'student/registration.html',{'sa':sea})

def Locker(request):
    lock=Login()
    return render(request,'student/login.html',{'lo':lock})