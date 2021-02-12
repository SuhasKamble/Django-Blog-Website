from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def login(request):
    return render(request, 'home/login.html')


def signup(request):
    return render(request, 'home/signup.html')
