from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page")

def my_blog(request):
    return HttpResponse("Hello, Blog!")
# Create your views here.
