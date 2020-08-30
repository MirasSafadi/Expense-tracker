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
        # print(dic)
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
                    request.session['current_user']=user.to_dict()
                    print('success')
                else:
                    print('failure: wrong password')
            else:
                print('failure: user does not exist')
        else:
            print('failure: form invalid')
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
                print('Error: User exists')
            elif password != password_confirmation:
                #check if passwords match
                print("Error: passwords don't match")
            else:
                #create a new user and save it in DB
                user = User(user_email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                #log the new user in
                request.session['current_user']=user.to_dict()
                print('success')
        else:
            print('failure: form invalid')
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