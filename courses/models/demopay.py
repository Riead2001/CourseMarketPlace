from django.db import models
from django.contrib.auth.models import User

class DemoPay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.course_name}"
