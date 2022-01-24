from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant
from django.urls import reverse


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the stores index.")

def home(request):
    # display a list of restaurants
    restaurant_objects = Restaurant.objects.all()

    context = {
        'restaurant_objects': restaurant_objects
    }
    return render(request, 'stores/home.html', context)

def storepage(request):
    restaurant_objects = Restaurant.objects.all()
    
    context = {
        'restaurant_objects': restaurant_objects
    }
    return render(request, 'stores/storepage.html', context)

def about(request):
    return HttpResponse("This is the about page.")

def menu(request):
    return HttpResponse("This is the menu page.")

def checkout(request):
    return HttpResponse("This is the checkout page.")