from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .course import Course


class Student(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields related to the student as needed

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz_mark = models.IntegerField(default=0)
    assignment_mark = models.IntegerField(default=0)

    @property
    def total_mark(self):
        return self.quiz_mark + self.assignment_mark

    # You can add other fields as needed

    def __str__(self):
        return f"{self.student.name}'s Marks"
