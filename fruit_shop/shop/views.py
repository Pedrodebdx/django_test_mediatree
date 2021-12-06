from django.http import HttpResponse
from django.shortcuts import render
from shop.models import *
from django.contrib.auth import authenticate, login  # login
from django.contrib.auth import logout  #logout
from django.contrib.auth.decorators import login_required



def index(request): # index with login
    if request.method == 'POST':
        formulaire_login= formulaire_login(request.POST)

    user = authenticate(request,user_id='admin', user_password='12345')
    if user is not None:
        login(request, user)
        print("LOG OK")
        return render(request, 'shop/market.html')
    else:
        print("NON LOG")
        return render(request, 'shop/index.html')   
     

# @login_required #décorateur pour authentification
def shop(request):
    products = Produits.objects.all()  
  
    return render(request, 'shop/market.html', {"products": products}) 

def logout_view(request):
    logout(request)
    return render(request, 'shop/logout.html')        