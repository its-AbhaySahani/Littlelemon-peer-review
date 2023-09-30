# from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def menu(request):
    menu_data = Menu.objects.order_by("name").all()
    main_data = {
        "menu": menu_data,
    }
    return render(request, 'menu.html', main_data)

def dish(request, name):
    try:
        dish = Menu.objects.get(name=name)
        return render(request, 'dish.html', context={
            "dish": dish
        })
    except Menu.DoesNotExist:
        return HttpResponse("Out of Stock")