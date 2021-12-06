from django.http import HttpResponse
from django.shortcuts import render
from shop.models import *


def shop(request):
    return render(request, 'shop/market.html')    


def index(request):
    return render(request, 'shop/market.html') 

def logout(request):
    return render(request, 'shop/logout.html')        