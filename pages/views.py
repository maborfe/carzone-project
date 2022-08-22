from django.shortcuts import HttpResponse, render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def login(request):
    return render(request, 'pages/login.html')


def signup(request):
    return render(request, 'pages/signup.html')
