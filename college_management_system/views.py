from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Teacher, Student

def teacher_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        subject = request.POST['subject']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        is_teacher = True
        teacher = Teacher.objects.create(
            username=username,
            password=password,
            name=name,
            subject=subject,
            phone_number=phone_number,
            email=email,
            is_teacher = is_teacher
        )
        return redirect('teacher_login')
    return render(request, 'teacher_signup.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Teacher, Student

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Teacher.objects.filter(username=username).first()
        print(user)
        if user is not None:
            if user.password == password:

                # Log the user in and redirect to success page
                authenticated_user = authenticate(request, username=username, password=password)
                login(request, authenticated_user)
                return redirect('college_management_system:teacher_list')

    else:
            error_message = "Invalid login credentials"
            return render(request, 'teacher_login.html', {'error_message': error_message})
    return render(request, 'teacher_login.html')


def student_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        roll_number = request.POST['roll_number']
        teacher_id = request.POST['teacher_id']
        teacher = Teacher.objects.get(id=teacher_id)
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        is_student = True
        student = Student.objects.create(
            username=username,
            password=password,
            name=name,
            roll_number=roll_number,
            teacher=teacher,
            phone_number=phone_number,
            email=email,
            is_student=is_student
        )
        return redirect('student_login')
    teachers = Teacher.objects.all()
    return render(request, 'student_signup.html', {'teachers': teachers})

def success(request):
    return render(request, 'success.html')

def success1(request):
    return render(request, 'success1.html')


def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Student.objects.filter(username=username).first()
        if user is not None:
            if user.password == password:
                # Log the user in and redirect to success page
                authenticated_user = authenticate(request, username=username, password=password)
                login(request, authenticated_user)
                return redirect('college_management_system:success')
        else:
            error_message = 'Invalid login credentials'
            return render(request, 'student_login.html', {'error_message': error_message})
    return render(request, 'student_login.html')




from django.shortcuts import render
from .models import Teacher

def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teacher_list.html', context)
