from django.shortcuts import redirect, render
from django.http import HttpResponse
from Expense_tracker import forms
from django.contrib import messages
from.models import User, Income, Outcome
import webbrowser

# Create your views here.
def home(request):
    dic = {}
    if 'current_user' in request.session:#if a user is logged in
        add_income_form = forms.Add_income_form()
        add_outcome_form = forms.Add_outcome_form()
        current_user = request.session['current_user']
        user = User.objects.get(user_email=current_user['user_email'])
        incomes_queryset = Income.objects.filter(user=user).order_by('-date')
        outcomes_queryset = Outcome.objects.filter(user=user).order_by('-date')
        balance = 0
        incomes = []
        outcomes = []
        for item in incomes_queryset:
            incomes.append(item)
            balance += item.amount
        for item in outcomes_queryset:
            outcomes.append(item)
            balance -= item.amount
        dic = {'current_user':current_user,
                'incomes':incomes,
                'outcomes':outcomes,
                'add_income_form':add_income_form,
                'add_outcome_form':add_outcome_form,
                'balance':balance,
                }
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

def delete_income(request,income_id):
    income = Income.objects.get(id=income_id)
    income.delete()
    return redirect('home')

def delete_outcome(request,outcome_id):
    outcome = Outcome.objects.get(id=outcome_id)
    outcome.delete()
    return redirect('home')

def add_income(request):
    if request.method == 'POST':
        add_income_form = forms.Add_income_form(request.POST)

        if 'current_user' in request.session:
            current_user = request.session['current_user']
            user = User.objects.get(user_email=current_user['user_email'])

            if add_income_form.is_valid():
                amount = add_income_form.cleaned_data['amount']
                isPeriodic = add_income_form.cleaned_data['isPeriodic']

                if amount <= 0:
                    messages.error(request,'Amount must be positive',extra_tags="add_income_error")
                else:
                    income = Income(user=user,amount = amount,isPeriodic=isPeriodic)
                    income.save()
            else:
               messages.error(request,'One or more of the fields is invalid!',extra_tags="add_income_error") 
    return redirect('home')

def add_outcome(request):
    if request.method == 'POST':
        add_outcome_form = forms.Add_outcome_form(request.POST)

    if 'current_user' in request.session:
        current_user = request.session['current_user']
        user = User.objects.get(user_email=current_user['user_email'])
        if add_outcome_form.is_valid():
            amount = add_outcome_form.cleaned_data['amount']
            isPeriodic = add_outcome_form.cleaned_data['isPeriodic']
            if amount <= 0:
                messages.error(request,'Amount must be positive',extra_tags="add_outcome_error")
            else:
                outcome = Outcome(user=user,amount = amount,isPeriodic=isPeriodic)
                outcome.save()
        else:
           messages.error(request,'One or more of the fields is invalid!',extra_tags="add_outcome_error") 
    return redirect('home')

def sendEmail(request):
    webbrowser.open('mailto:safadimiras@gmail.com?subject=Expense Tracker inquiry', new=2)
    return HttpResponse('<script>history.back();</script>')