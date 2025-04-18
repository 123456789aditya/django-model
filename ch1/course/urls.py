from django.contrib import admin
from django.urls import path
from course.views import learn_d,learn_p

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj/',learn_d,name='django'),
    path('py/',learn_p,name='python')
   
]
