# forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        email = cleaned_data.get("email")
        
        # Check if passwords match
        if password and password_confirm and password != password_confirm:
            raise ValidationError("Passwords do not match")
        
        # Check if email is already in use
        if email and User.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered")
        
        # Check if username is already in use
        if username and User.objects.filter(username=username).exists():
            raise ValidationError("Username is already taken")

        return cleaned_data

    def save(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        return user