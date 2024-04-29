from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from courses.models.customuser import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=50)
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'role']

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("User with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = self.cleaned_data['role']  # Set the role from the form data
        if commit:
            user.save()
        # Save data in the default User model
        default_user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        default_user.first_name = self.cleaned_data['first_name']
        default_user.last_name = self.cleaned_data['last_name']
        default_user.save()
        return user
