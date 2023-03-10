from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Teacher(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students')
    phone_number = PhoneNumberField()
    email = models.EmailField()

    def __str__(self):
        return self.name
