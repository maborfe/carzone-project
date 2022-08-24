from django.shortcuts import HttpResponse, render

from .models import *


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def login(request):
    return render(request, 'pages/login.html')

def signup(request):
    return render(request, 'pages/signup.html')

def about(request):
    return render(request, 'pages/about.html')

def cars(request):
    return render(request, 'pages/cars.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

def search(request):
    return render(request, 'pages/search.html')
    
def about(request):
    template = 'pages/about.html'
    context = dict()
    team_members = Team.objects.all()
    context = {'team_members': team_members}    
    
    return render(request, template, context)

def car_details(request):
    return render(request, 'pages/car_details.html')


