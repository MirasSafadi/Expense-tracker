from django.contrib import admin
from django.urls import path,include
from Expense_tracker import views as v

urlpatterns = [
    path('', v.home, name="home"),
    path('/about', v.about, name="about"),
    path('sendEmail', v.sendEmail),
    path('login', v.login),
    path('signup', v.signup),
]
