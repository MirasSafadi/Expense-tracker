from django import forms
from Expense_tracker import models

class LoginForm(forms.Form):
    email = forms.CharField(required = True, max_length = 254, widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'enter your email'}))
    password = forms.CharField(required = True, widget = forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'enter your password'}))