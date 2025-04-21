from django.shortcuts import render

# Create your views here.
from student.forms import Registration

def Final(request):
    sea=Registration()
    return render(request,'student/registration.html',{'sa':sea})