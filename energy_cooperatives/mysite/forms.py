from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
