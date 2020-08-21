from django.shortcuts import render
from django.http import HttpResponse
import webbrowser

# Create your views here.
def home(request):
    # return HttpResponse("Testing Django")
    return render(request,'base.html')
def about(request):
    # return HttpResponse("Testing Django")
    return render(request,'About.html')
def sendEmail(request):
    webbrowser.open('mailto:', new=1)