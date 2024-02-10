# compEng/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import FacultyUser
from django import forms
from .models import StudentMark

class UserCreationForm(UserCreationForm):
    class Meta:
        model = FacultyUser
        fields = ['username', 'name', 'phone_number', 'password1', 'password2']

class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = FacultyUser
        fields = ['username', 'password']



class StudentMarkForm(forms.ModelForm):
    class Meta:
        model = StudentMark
        fields = ['name', 'roll', 'mark1', 'mark2', 'mark3']
