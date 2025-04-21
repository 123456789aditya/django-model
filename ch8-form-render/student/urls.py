from django.contrib import admin
from django.urls import path
from student.views import Final
urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/',Final)
]
