from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class CustomUser(AbstractUser):
    # Your custom fields here
    date_of_birth = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    college_name = models.CharField(max_length=100, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_users',
        blank=True,
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        related_query_name='custom_user',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    class Meta:
        permissions = (("can_view_custom", "Can view custom"),)
