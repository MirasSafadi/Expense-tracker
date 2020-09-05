from django.contrib import admin
from django.urls import path,include
from Expense_tracker import views as v

urlpatterns = [
    path('', v.home, name="home"),
    path('/about', v.about, name="about"),
    path('sendEmail', v.sendEmail),
    path('login', v.login),
    path('signup', v.signup),
    path('logout', v.logout),
    path('add_income', v.add_income),
    path('add_outcome', v.add_outcome),
    path('deleteIncome/<income_id>', v.delete_income),
    path('deleteOutcome/<outcome_id>', v.delete_outcome),
]
