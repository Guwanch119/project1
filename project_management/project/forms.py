from django import forms
from django.contrib.auth.forms import AuthenticationForm

class studentloginform(AuthenticationForm):
    username = forms.CharField(label="Student Name")
    password = forms.CharField(label="Parol",widget=forms.PasswordInput)