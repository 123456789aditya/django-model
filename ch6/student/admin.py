
from django.contrib import admin
from student.models import profile,biodata
#Register your models here.

class profileAdmin(admin.ModelAdmin):
    list_display=('name','roll','email','city')
    
admin.site.register(profile,profileAdmin)