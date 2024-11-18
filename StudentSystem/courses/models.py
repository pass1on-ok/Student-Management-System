from django.db import models
from users.models import CustomUser
from students.models import Student

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.ForeignKey(CustomUser, limit_choices_to={'role': 'teacher'}, on_delete=models.CASCADE)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)