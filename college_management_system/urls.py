from django.urls import path

from . import views
from .views import teacher_signup,teacher_login,student_signup,student_login
from django.urls import path


app_name = 'college_management_system'


urlpatterns = [
    path('',views.student_signup, name= 'student_signup'),
    path('student_login',views.student_login, name= 'student_login'),
    path('success',views.success,name = 'success'),
    path('success1',views.success1,name = 'success1'),
    path('teacher_login',views.teacher_login, name= 'teacher_login'),
    path('teacher_signup',views.teacher_signup, name= 'teacher_signup'),
    path('teacher_list',views.teacher_list, name= 'teacher_list'),
]
