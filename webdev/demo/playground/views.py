from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# request handler
# action
def homepage_view(*args, **kwargs):
    return HttpResponse('<h1>You are looking at the home page! :) </h1>')

def contact_view(*args, **kwargs):
    return HttpResponse('<h1>This is the contact page, ring ring!</h1>')

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Michael'})