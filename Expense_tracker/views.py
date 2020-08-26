from django.shortcuts import redirect, render
from django.http import HttpResponse
from Expense_tracker import forms
from.models import User
import webbrowser

# Create your views here.
def home(request):
    dic = {}
    if 'current_user' in request.session:
        user = request.session['current_user']
        dic = {'current_user':user}
    return render(request,'home.html',dic)
def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            if User.objects.filter(user_email=email).exists():
                user = User.objects.get(user_email=email)
                if user.password == password:
                    #add user to session and redirect
                    print('success')
                    request.session['current_user']=user.__dict__
                else:
                    print('failure: wrong password')
            else:
                print('failure: user does not exist')
        else:
            print('failure: form invalid')

    return render(request,'home.html')
def signup(request):
    if request.method == 'POST':
        signup_form = forms.SignupForm(request.POST)
        if signup_form.is_valid():
            print(signup_form.cleaned_data['email'],'\n')
            print(signup_form.cleaned_data['password'],'\n')
            print(signup_form.cleaned_data['first_name'],'\n')
            print(signup_form.cleaned_data['last_name'],'\n')
    return HttpResponse('<script>history.back();</script>')
        
def about(request):
    # return HttpResponse("Testing Django")
    return render(request,'About.html')
def sendEmail(request):
    webbrowser.open('mailto:safadimiras@gmail.com?subject=Expense Tracker inquiry', new=2)
    return HttpResponse('<script>history.back();</script>')