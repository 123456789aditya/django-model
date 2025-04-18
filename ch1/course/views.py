from django.shortcuts import render

# Create your views here.
def learn_d(request):
    return render(request,'course/d.html')

def learn_p(request):
    return render(request,'course/p.html')