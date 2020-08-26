from django import forms
from Expense_tracker import models

class LoginForm(forms.Form):
    
    email = forms.EmailField(required = True, max_length = 254, widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'enter your email'}))
    password = forms.CharField(required = True, widget = forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'enter your password'}))
    required_css_class = 'required'

class SignupForm(forms.Form):
    
    email = forms.EmailField(required = True, max_length = 254, widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'enter your email'}))
    first_name = forms.CharField(required = True, widget = forms.TextInput(attrs={'class' : 'form-control','placeholder':'enter your first name'}))
    last_name = forms.CharField(required = True, widget = forms.TextInput(attrs={'class' : 'form-control','placeholder':'enter your last name'}))
    password = forms.CharField(required = True, widget = forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'enter your password'}))
    password_confirmation = forms.CharField(label='Confirm password',required = True, widget = forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'re-enter your password'}))
    required_css_class = 'required'