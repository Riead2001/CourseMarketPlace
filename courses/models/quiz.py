# In your models.py file

from django.db import models
from django.contrib.auth.models import User
from .user_course import UserCourse
from .course import Course

class Quiz(models.Model):
    course_name = models.CharField(max_length=100)
    quiz_number = models.IntegerField()
    quiz_link = models.URLField()

    def __str__(self):
        return f"{self.course_name} - Quiz {self.quiz_number}"
