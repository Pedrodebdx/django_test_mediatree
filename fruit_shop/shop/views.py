from django.http import HttpResponse
from django.shortcuts import render
from shop.models import *

def index(request): 
    return render(request, 'shop/index.html')  # to return the index view, after login

def shop(request):
    return render(request, 'shop/market.html')   # to return market page, after login 

def logout(request):
    return render(request, 'shop/logout.html')        