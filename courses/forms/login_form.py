from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

class LoginForm(AuthenticationForm):

    username = forms.EmailField(max_length=50, required=True, label='Email Address')
    role = forms.ChoiceField(choices=(('student', 'Student'), ('instructor', 'Instructor')), label='Role')

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        role = self.cleaned_data.get('role')

        user = None
        try:
            UserModel = get_user_model()  # Renamed 'User' to 'UserModel'
            user = UserModel.objects.get(email=email)
            result = authenticate(username=user.username, password=password)
            if result is not None:
                self.cleaned_data['user'] = result  # Store the authenticated user in cleaned_data
                self.cleaned_data['role'] = role  # Store the selected role in cleaned_data
                return self.cleaned_data
            else:
                raise ValidationError("Email or Password Invalid")
        except UserModel.DoesNotExist:
            raise ValidationError("Email or Password Invalid")