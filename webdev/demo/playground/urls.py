from django.urls import path
from . import views

# URLconf module
urlpatterns = [
    path('hello/', views.say_hello)
]