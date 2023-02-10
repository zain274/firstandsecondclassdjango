from django.http import HttpResponse
from django.shortcuts import render,redirect


def function1(request):
    return HttpResponse("any")

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"About.html")



def contact(request):
    return render(request,"Contact.html")

def portfolio(request):
    return render(request,"Portfolio.html")

def team(request):
    return render(request,"Team.html")