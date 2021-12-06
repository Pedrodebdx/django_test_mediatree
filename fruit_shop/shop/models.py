from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Produits(models.Model): # types of products

    class Type(models.TextChoices): # for menu 
        FRUIT = 'Fruit'
        VEGETABLES = 'Légumes'
       
          
    name = models.fields.CharField(max_length=100)
    type = models.fields.CharField(choices=Type.choices, max_length=10) # for menu 
    price = models.fields.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)]) # validators to validate if price could exist
    stock = models.IntegerField()
    picture_url = models.fields.URLField(null=True, blank=True)


class User(models.Model):
    user_id = models.fields.CharField(max_length=100)
    user_password = models.fields.CharField(max_length=100)