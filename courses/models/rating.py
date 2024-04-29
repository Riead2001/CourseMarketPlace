from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    coursename = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    review = models.TextField()

    def __str__(self):
        return f"{self.username.username} - {self.coursename}"
