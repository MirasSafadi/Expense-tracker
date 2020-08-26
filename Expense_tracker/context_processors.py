from Expense_tracker import forms

def get_login_form(request):
    return {'login_form':forms.LoginForm()}
def get_signup_form(request):
    return {'signup_form':forms.SignupForm()}