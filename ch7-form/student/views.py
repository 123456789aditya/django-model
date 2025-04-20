from django.shortcuts import render

# Create your views here.
from student.forms import Registration
def registration(request):
    fm=Registration()
    return render(request,'student/registration.html',{'form':fm})