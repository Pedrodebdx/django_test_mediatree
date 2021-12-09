from django.http import HttpResponse
from django.shortcuts import redirect, render
from shop.models import *
from django.contrib.auth import authenticate, login  # login
from django.contrib.auth import logout  #logout
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required # to restrict page of market
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def index(request): # index with login
    
    if request.method == 'POST':
        print("requete POST")
        user_id          = request.POST.get('user_id')
        user_password    = request.POST.get('user_password')
        user = authenticate(request,user_id=user_id, user_password=user_password)
        
        login(request, user)
        if user is not None:
            login(request, user)
            print("LOG OK")
        # return render(request, 'shop/market.html')

    if request.method == 'GET':
        print("requete GET")
        return render(request, 'shop/index.html')
    

    else:
        print("NON LOG")
        return render(request, 'shop/index.html')
     

@login_required #decorator to  restrict page of market
def shop(request):
    products = Produits.objects.all().order_by('stock')  #select all product of db and order by stock
    return render(request, 'shop/market.html', {"products": products}) #return html page ans dictionnary of products


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Nouvel utilisateur crée, vous pouvez maintenant vous loguer")
            return render(request, 'shop/index.html')
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form":form})   


def logout_view(request):
    logout(request)
    return render(request, 'logout/')        