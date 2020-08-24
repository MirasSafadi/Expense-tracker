from django.shortcuts import redirect, render
from django.http import HttpResponse
from Expense_tracker import forms
import webbrowser

# Create your views here.
def home(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            print(login_form.cleaned_data['email'],'\n')
            print(login_form.cleaned_data['password'],'\n')
    else:
        login_form = forms.LoginForm()

    return render(request,'home.html',{'login_form':login_form})
def about(request):
    # return HttpResponse("Testing Django")
    return render(request,'About.html')
def sendEmail(request):
    webbrowser.open('mailto:safadimiras@gmail.com?subject=Expense Tracker inquiry', new=2)
    return HttpResponse('<script>history.back();</script>')