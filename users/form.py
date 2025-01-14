from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import re




class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-control'
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm password'
        })
    )

    class Meta:
        model = CustomUser 
        fields = ['first_name', 'last_name', 'username', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Enter first name',
            'last_name': 'Enter last name',
            'username': 'Enter user name'
        }
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders.get(field, '')

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)  # Django's built-in password validation
        return password


    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 2:
            raise ValidationError('First name must be at least 5 characters long.')
        if re.match(r'^[a-zA-Z]+$', first_name) is None:
            raise ValidationError('First name cannot consist solely of special characters.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if re.match(r'^[a-zA-Z]+$', last_name) is None:
            raise ValidationError('Last name cannot consist solely of special characters.')
        return last_name

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')

        username = cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('This username address is already registered.')

        return cleaned_data


from django import forms
from django.contrib.auth.models import User

class PasswordResetForm(forms.Form):
    first_name = forms.CharField(max_length=150, required=True, label="First Name")
    last_name = forms.CharField(max_length=150, required=True, label="Last Name")
    new_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="New Password",
        max_length=128
    )

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        # Check if a user with the provided first and last name exists
        if not CustomUser.objects.filter(first_name=first_name, last_name=last_name).exists():
            raise forms.ValidationError("No user found with the provided first and last name.")
        return cleaned_data

    def save(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        new_password = self.cleaned_data['new_password']

        # Retrieve the user and reset the password
        user = CustomUser.objects.get(first_name=first_name, last_name=last_name)
        user.set_password(new_password)
        user.save(update_fields=['password'])  # Trigger the signal

    
