from django.contrib import admin
from django.urls import path
from student.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/',register,name='register')
]
