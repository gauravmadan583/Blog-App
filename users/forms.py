from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(label='First Name', min_length=3, max_length=10)
    lastname = forms.CharField(label='Last Name', min_length=3, max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    firstname = forms.CharField(min_length=3, max_length=10)
    lastname = forms.CharField(min_length=3, max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']