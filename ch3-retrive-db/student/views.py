from django.shortcuts import render
from student.models import profile


# Create your views here.
def all_data(request):
    students=profile.objects.all()
    return render(request,'student/all.html',{'stu':students})

def single_data(request):
    stud1=profile.objects.get(pk=1)
    return render(request,'student/single.html',{'stud':stud1})