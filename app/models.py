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