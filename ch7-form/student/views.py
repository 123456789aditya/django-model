from django.shortcuts import render

# Create your views here.
from student.forms import Registration,Login
def registration(request):
    fm=Registration(field_order=['email','city'])
    return render(request,'student/registration.html',{'form':fm})

def login(request):
    lg=Login(initial={'userid':'sonam@gmail.com'})
    return render(request,'student/login.html',{'login':lg})