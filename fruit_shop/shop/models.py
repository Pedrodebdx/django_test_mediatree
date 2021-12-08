from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Produits(models.Model): # types of products

    class Type(models.TextChoices): # for menu 
        FRUIT = 'Fruit'
        VEGETABLES = 'Légumes'
       
          
    name = models.fields.CharField(max_length=100)
    type_produit = models.fields.CharField(choices=Type.choices, max_length=10) # for menu 
    price = models.fields.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)]) # validators to validate if price could exist
    stock = models.IntegerField()
    picture_url = models.fields.URLField(null=True, blank=True)


# class User(models.Model):
#     REQUIRED_FIELDS = ('user_id','user_password')
#     user_id = models.fields.CharField(max_length=100, unique=True)
#     user_password = models.fields.CharField(max_length=100)

# from django import forms

# class LoginForm(forms.Form):
#     user_id = forms.CharField(required=True,max_length=100)
#     password = forms.CharField(required=True,max_length=100)