from django.db import models
from courses.models import Course
from students.models import Student
from users.models import CustomUser

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    teacher = models.ForeignKey(CustomUser, limit_choices_to={'role': 'teacher'}, on_delete=models.CASCADE)