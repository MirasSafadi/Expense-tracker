from django.shortcuts import redirect, render
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
    webbrowser.open('mailto:safadimiras@gmail.com?subject=Expense Tracker inquiry', new=2)
    return HttpResponse('<script>history.back();</script>')