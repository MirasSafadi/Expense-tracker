from django.contrib import admin
from django.urls import path,include
from Expense_tracker import views

urlpatterns = [
    path('', views.home, name="home"),
    path('/about', views.about, name="about"),
    path('/sendEmail', views.sendEmail, name="sendEmail"),
]
