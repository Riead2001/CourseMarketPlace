from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.db import models

class Scholarship(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    coursename = models.CharField(max_length=100, null=True)  # Making coursename nullable
    
    reason = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.username.username} - {self.coursename}"
