from django.shortcuts import render
from student.forms import Registration

# Create your views here.
def register(request):
    if request.method=='POST':
        regr=Registration(request.POST)
        print(regr)
    reg=Registration()
    return render(request,'student/registration.html',{'regr':reg})