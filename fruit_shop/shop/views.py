from django.http import HttpResponse
from django.shortcuts import render
from shop.models import *
from django.contrib.auth import authenticate, login  # login
from django.contrib.auth import logout  #logout
from django.contrib.auth.decorators import login_required



def index(request): # index with login
    try:
        user_id = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=user_id, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'shop/market.html')   # to return market page, after login 
        else:
            return HttpResponse('<h1>Utilisateur ou mot de passe invalide, faite retour pour réessayer/h1>')    
    except:
        return HttpResponse('<h1>PASS : Utilisateur ou mot de passe invalide, faite retour pour réessayer/h1>')           

# @login_required #décorateur pour authentification
def shop(request):
    products = Produits.objects.all()  
  # if not request.user.is_authenticated:
    #    return render(request, 'shop/market.html', produits)   # to return market page, after login 
    # if not request.user.is_authenticated:
    #     return render(request, 'index.html')
   
    return render(request, 'shop/market.html', {"products": products}) 

def logout_view(request):
    logout(request)
    return render(request, 'shop/logout.html')        