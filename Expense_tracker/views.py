from django.shortcuts import redirect, render
from django.http import HttpResponse
from Expense_tracker import forms
from django.contrib import messages
from.models import User
import webbrowser

# Create your views here.
def home(request):
    dic = {}
    if 'current_user' in request.session:
        user = request.session['current_user']
        dic = {'current_user':user}
        # print(dic)
    return render(request,'home.html',dic)
def login(request):
    isError = True
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            if User.objects.filter(user_email=email).exists():
                user = User.objects.get(user_email=email)
                if user.password == password:
                    #add user to session and redirect
                    request.session['current_user']=user.to_dict()
                    isError = False
            if isError: #Wrong credentials
                messages.error(request,'Wrong email/password',extra_tags="login_error")
                return HttpResponse('<script>history.back();</script>')
        else:#form invalid
            messages.error(request,'Invalid email/password field',extra_tags="login_error")
            return HttpResponse('<script>history.back();</script>')
    return redirect('home')
def signup(request):
    if request.method == 'POST':
        signup_form = forms.SignupForm(request.POST)
        if signup_form.is_valid():
            email = signup_form.cleaned_data['email']
            first_name = signup_form.cleaned_data['first_name']
            last_name = signup_form.cleaned_data['last_name']
            password = signup_form.cleaned_data['password']
            password_confirmation = signup_form.cleaned_data['password_confirmation']

            if User.objects.filter(user_email=email).exists():
                #check if user exists
                messages.error(request,'User exists',extra_tags="signup_error")
            elif password != password_confirmation:
                #check if passwords match
                messages.error(request,"Passwords don't match",extra_tags="signup_error")
            else:
                #create a new user and save it in DB
                user = User(user_email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                #log the new user in
                request.session['current_user']=user.to_dict()

        else:
            messages.error(request,"One or more of the fields is invalid.",extra_tags="signup_error")
    return redirect('home')
def logout(request):
    try:
        del request.session['current_user']
    except KeyError:
        return HttpResponse("<h1>Internal Server Error</h1></br><p>Could not find 'current_user' in session")
    # print(request.session['current_user'])
    return redirect('home')
def about(request):
    dic = {}
    if 'current_user' in request.session:
        user = request.session['current_user']
        dic = {'current_user':user}
        # print(dic)
    return render(request,'About.html',dic)
def sendEmail(request):
    webbrowser.open('mailto:safadimiras@gmail.com?subject=Expense Tracker inquiry', new=2)
    return HttpResponse('<script>history.back();</script>')