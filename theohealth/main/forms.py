from django.forms import ModelForm
from django import forms
from main.models import Athlete

class AddAthleteForm(ModelForm):
    class Meta:
        model = Athlete
        fields = ['first_name', 'last_name', 'contact_nb', 'email', 'phone_nb', 'injury']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'contact_nb':'Contact', 'phone_nb':'Phone', 'injury': 'Details on Injury',}

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(label='Password', max_length=64, widget=forms.PasswordInput)
