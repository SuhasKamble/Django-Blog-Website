from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("This is home page")


def about(request):
    return HttpResponse("This is about page")


def contact(request):
    return HttpResponse("This is ConTact Page")


def login(request):
    return HttpResponse("This is login")


def signup(request):
    return HttpResponse("This is signup")
