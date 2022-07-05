from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# request handler
# action
def homepage_view(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse('<h1>You are looking at the home page! :) </h1>')
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    # return HttpResponse('<h1>This is the contact page, ring ring!</h1>')
    my_context = {
        "my_text": "Learn about me!",
        "my_number": "647 551 7917",
    }
    return render(request, 'contact.html', my_context)

def about_view(request, *args, **kwargs):
    # return HttpResponse('<h1>This is the about page, let me tell you about myself!</h1>')
    my_about = {
        "my_list": ["I'm an undergraduate at UofT", "I'm learning web development", "I like to use Python"],
    }
    return render(request, 'about.html', my_about)

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Michael'})