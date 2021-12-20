from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Recipe(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=50)
    image_url = models.CharField(max_length=400)
    tags = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

class DayMenu(models.Model):
    title = models.CharField(max_length=30)
    breakfast = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="breakfasts")
    meal = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="meals" )
    dinner = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="dinners")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")

    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} | {self.price} "




class ZoneProduct(models.Model):
   
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    category = models.CharField(max_length=20)
    blocks = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.price} | {self.category}"

class ZoneMenu(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    ratio = models.FloatField(default=0)
   
    def __str__(self):
        return f"{self.name}"


class Item(models.Model):
    menu = models.ForeignKey(ZoneMenu, on_delete=models.CASCADE)
    product = models.ForeignKey(ZoneProduct, on_delete=models.CASCADE )

    def __str__(self):
        return f"{self.product.name}"
