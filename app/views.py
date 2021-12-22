from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import User, ZoneDay, ZoneMenu


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
    breakfast = random.choice(breakfasts)

    meals = Recipe.objects.filter(tags__contains="comida")
    meal = random.choice(meals)

    dinners = Recipe.objects.filter(tags__contains="cena")
    dinner = random.choice(dinners)

    recipes = [breakfast, meal, dinner]

    return render(request, 'app/random_menu.html',{
        'recipes': recipes
    })

def random_week(request):

    breakfasts = Recipe.objects.filter(tags__contains="desayuno")
    meals = Recipe.objects.filter(tags__contains="comida")
    dinners = Recipe.objects.filter(tags__contains="cena")

    week_menus = []

    for day in range(6):
        title = f"Day {day+1}"
        breakfast = random.choice(breakfasts)
        meal = random.choice(meals)
        dinner = random.choice(dinners)

        day_menu = DayMenu(title=title, 
                       breakfast=breakfast, meal=meal, dinner=dinner,
                       creator=request.user)

        week_menus.append(day_menu)


    return render(request, 'app/random_week.html',{
        'menus': week_menus
    })

import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_fat(request):
    if request.method == 'GET':
        return render(request, "app/get_fat.html")
    
    if request.method == 'POST':
        payload = json.loads(request.body)
        
        height = int(payload['height'])
        weight = int(payload['weight'])
        age =  int(payload['age'])
        gender =  payload['gender']
        print('-->', gender)

       
        imc = indice_masa_corporal(height, weight)

        if imc > 21 and imc < 25:
            imc_message = "good"
        elif imc <= 21:
            imc_message = "low"
        elif imc >= 25:
            imc_message = "hight"

        fbp = fat_body_porcentaje(imc, age, int(gender))
        fbp_message = analize_fbp(fbp, int(gender) )

        return JsonResponse({'imc': imc,
                             'imc_message': imc_message,
                             'fbp': fbp,
                             'fbp_message': fbp_message})

def indice_masa_corporal(height, weight):
     imc = weight/((height/100)**2)
     return  round(imc, 3)

def fat_body_porcentaje(imc, age, gender):
    fbp = (1.39 * imc) + (0.16 * age) - (10.34 * gender) - 9
    return round(fbp, 2)

def analize_fbp(fbp, gender):
    if gender == 1:
        if fbp < 7:
            return 'low'
        elif fbp > 22:
            return 'hight'
        else:
            return 'good'
    if gender == 0:
        if fbp < 13:
            return 'low'
        elif fbp > 22:
            return 'hight'
        else:
            return 'good'

from app.models import Product
def shopping_list(request):

    products = Product.objects.all()

    return render(request, 'app/shopping_list.html',{
        'products': products
    })

@csrf_exempt
def add_product(request):

    if request.method == 'POST':
        payload = json.loads(request.body)
        
        name = payload['name']
        price = payload['price']

        product = Product(name=name, price=price)
        product.save()

        return JsonResponse({'msg':'product added',
                             'product_id': product.id})

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()

    return redirect('shopping_list')

def check_uncheck(request, product_id):
    product = Product.objects.get(pk=product_id)

    product.checked = not product.checked
    product.save()

    return redirect('shopping_list')

@csrf_exempt
def update_product(request):

    if request.method == 'POST':
        payload = json.loads(request.body)
        
        new_name = payload['new_name']
        new_price = payload['new_price']
        product_id = payload['product_id']

        product = Product.objects.get(pk=product_id)
        product.name = new_name
        product.price = new_price
        product.save()

        return JsonResponse({'msg':'product updated',
                             'product_id': product.id
                             })

### ZONE ###
from .models import ZoneProduct
def zone_add_product(request):

    if request.method == 'GET':
        products = ZoneProduct.objects.all()
        return render(request, 'app/zone_add_product.html', {
            'products': products
        })

    if request.method == 'POST':
            
        product = ZoneProduct(name  = request.POST['name'],
                              price = int(request.POST['price']),
                              category = request.POST['category'],
                              blocks = int(request.POST['blocks']) )
        product.save()

        #return JsonResponse(request.POST)
        return redirect('zone_add_product')

def zone_create_menu(request):
    
    if request.method == 'GET':

        proteins = ZoneProduct.objects.filter(category__contains="protein")
        carbs = ZoneProduct.objects.filter(category__contains="carb")
        fats = ZoneProduct.objects.filter(category__contains="fat")

        menus = ZoneMenu.objects.all()

        return render(request, 'app/zone_create_menu.html',{
            'proteins': proteins,
            'carbs': carbs,
            'fats': fats,
            'menus': menus
        })

    if request.method == 'POST':
        menu = ZoneMenu(name=request.POST['menu_name'])
        menu.save()

        protein = ZoneProduct.objects.get(pk=int(request.POST['protein_id']))
        carb = ZoneProduct.objects.get(pk=int(request.POST['carb_id']))
        fat = ZoneProduct.objects.get(pk=int(request.POST['fat_id']))
        menu.item_set.create(product=protein)
        menu.item_set.create(product=carb)
        menu.item_set.create(product=fat)

        menu.price = protein.price + carb.price + fat.price
        menu.ratio = protein.blocks / carb.blocks

        menu.save()

        return redirect('zone_menus')

def zone_menus(request):
    if request.method == 'GET':
        menus = ZoneMenu.objects.all()

        return render(request, 'app/zone_menus.html', {
            'menus': menus
        })

def zone_menu(request, menu_id):
    menu = ZoneMenu.objects.get(pk=int(menu_id))

    return render(request, 'app/zone_menu.html',{
        'menu': menu
    })

def zone_create_day(request):
    if request.method == 'GET':
        meals = ZoneMenu.objects.exclude(tags__contains="snack")
        snacks = ZoneMenu.objects.filter(tags__contains="snack")

        return render(request, 'app/zone_create_day.html',{
            'meals': meals,
            'snacks': snacks
        })

    if request.method == 'POST':

        breakfast = ZoneMenu.objects.get(pk=int(request.POST['breakfast_id']))
        snackI = ZoneMenu.objects.get(pk=int(request.POST['snackI_id']))
        meal = ZoneMenu.objects.get(pk=int(request.POST['meal_id']))
        snackII = ZoneMenu.objects.get(pk=int(request.POST['snackII_id']))
        dinner = ZoneMenu.objects.get(pk=int(request.POST['dinner_id']))


        day = ZoneDay(name = request.POST['day_name'],
                      breakfast = breakfast,
                      snackI = snackI,
                      meal = meal,
                      snackII = snackII,
                      dinner = dinner
                      )

        day.save()

        return JsonResponse(request.POST)

def zone_days(request):
    days = ZoneDay.objects.all()

    return render(request, 'app/zone_days.html',{
        'days': days
    })