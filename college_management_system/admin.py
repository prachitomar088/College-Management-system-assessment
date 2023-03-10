from django.contrib import admin

# Register your models here.
from college_management_system.models import Student,Teacher

admin.site.register(Teacher)
admin.site.register(Student)