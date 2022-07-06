from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm, RawProductForm
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

# product view

def product_create_view(request):
    my_form = RawProductForm(request.GET)
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form

    }
    return render(request, 'product/product_create.html', context)

# def product_create_view(request):
#     # GET is a dictionary
#     # POST is safer than GEt
#     my_new_title = request.POST.get('title')
    
#     context = {
#     }
#     return render(request, 'product/product_create.html', context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context = {
#         'form': form
#     }
#     return render(request, 'product/product_create.html', context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'product/detail.html', context)