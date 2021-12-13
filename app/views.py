from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import User


def index(request):
    recipies = Recipe.objects.all()
    return render(request, "app/index.html", {
        'recipes': recipies
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "app/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "app/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "app/register.html")

from app.models import Recipe, DayMenu
def add_recipe(request):
    if request.method == 'GET':
        return render(request, 'app/add_recipe.html')

    if request.method == 'POST':
        title = request.POST['title']
        ingredients = request.POST['ingredients']
        description = request.POST['description']
        image_url = request.POST['image_url']
        tags = request.POST['tags']

        new_recipe_obj = {
            'title': title,
            'ingredients': ingredients,
            'description': description,
            'image_ur': image_url,
            'tags': tags
        }

        new_recipe = Recipe(title=title, ingredients=ingredients, description=description, 
                            image_url=image_url, tags=tags, creator=request.user)
        new_recipe.save()


        #return JsonResponse(new_recipe_obj)
        return redirect('index')

def filter_by_tag(request, tag):
    recipes = Recipe.objects.filter(tags__contains=tag)

    return render(request, 'app/filter.html', {
        'recipes': recipes,
        'tag': tag
    })

def edit_recipe(request, recipe_id):

    if request.method == 'GET':

        recipe = Recipe.objects.get(pk=recipe_id)

        return render(request, 'app/edit_recipe.html', {
            'recipe': recipe
        })
   
    if request.method == 'POST':
        new_version = request.POST

        recipe = Recipe.objects.get(pk=recipe_id)

        recipe.title = new_version['title']
        recipe.image_url = new_version['image_url']
        recipe.description = new_version['description']
        recipe.ingredients = new_version['ingredients']
        recipe.tags = new_version['tags']

        recipe.save()


        #return JsonResponse(new_version)
        #return redirect('index')
        return HttpResponseRedirect( reverse('recipe', args=(recipe.id,)) )

def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    recipes = Recipe.objects.filter(creator=user_id)

    return render(request, 'app/profile.html', {
        'recipes': recipes,
        'profile_user': user
    })

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)

    return render(request, 'app/recipe.html', {
        'recipe': recipe
    } )

def add_menu(request):

    if request.method == 'GET':
        breakfasts = Recipe.objects.filter(tags__contains='desayuno')
        meals = Recipe.objects.filter(tags__contains='comida')
        dinners = Recipe.objects.filter(tags__contains='cena')

        return render(request, 'app/add_menu.html',{
            'breakfasts': breakfasts,
            'meals': meals,
            'dinners': dinners
        })

    if request.method == 'POST':
        title = request.POST['title']
        breakfast_id = request.POST['breakfast']
        meal_id = request.POST['meal']
        dinner_id = request.POST['dinner']

        breakfast = Recipe.objects.get(pk=breakfast_id)
        meal = Recipe.objects.get(pk=meal_id)
        dinner = Recipe.objects.get(pk=dinner_id)

        menu = DayMenu(title=title, 
                       breakfast=breakfast, meal=meal, dinner=dinner,
                       creator=request.user)
        menu.save()

        return redirect('show_menus')

def show_menus(request):
    menus = DayMenu.objects.all()
    return render(request, 'app/menus.html',{
        'menus': menus
    })

def edit_menu(request, menu_id):

    if request.method == 'GET':
        menu = DayMenu.objects.get(pk=menu_id)

        breakfasts = Recipe.objects.filter(tags__contains='desayuno')
        meals = Recipe.objects.filter(tags__contains='comida')
        dinners = Recipe.objects.filter(tags__contains='cena')


        return render(request, 'app/edit_menu.html',{
            'menu': menu,
            'breakfasts': breakfasts,
            'meals': meals,
            'dinners': dinners
        })
    
    if request.method == 'POST':
        menu = DayMenu.objects.get(pk=menu_id)

        menu.title = request.POST['title']
        menu.breakfast = Recipe.objects.get(pk = request.POST['breakfast'])
        menu.meal = Recipe.objects.get(pk = request.POST['meal'])
        menu.dinner = Recipe.objects.get(pk = request.POST['dinner'])

        menu.save()
        
        return HttpResponseRedirect(reverse('show_menus'))

import random
def random_recipe(request):

    recipes = Recipe.objects.all()
    recipe = random.choice( recipes )

    return render(request, 'app/random_recipe.html',{
        'recipe': recipe
    })

def random_menu(request):

    breakfasts = Recipe.objects.filter(tags__contains="desayuno")

    return render(request, 'app/random_menu.html',{
        'recipes': breakfasts
    })
    #return render(request, 'app/random_menu.html')