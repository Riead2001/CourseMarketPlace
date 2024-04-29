from django import forms
from django.contrib.auth.forms import UserCreationForm
from courses.models.customuser import CustomUser  # Import your CustomUser model

class CustomUserCreationForm(UserCreationForm):
    # Define the additional fields you want to include in the form
    role = forms.CharField(max_length=20)  # Adjust field type as needed

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'role')  # Include 'role' field here
