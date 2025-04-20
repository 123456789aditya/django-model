from django.contrib import admin
from django.urls import path
from student.views import registration,login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/',registration),
    path('login/',login)
]