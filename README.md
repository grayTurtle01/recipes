# Description
This a a Web-App for recipes and health.

## Requirements
- [x] The application is sufficiently distict the other projects
- [x] The projects isn't a social network
- [x] The projects isn't a e-commerce
- [x] The application use Django from back-end
- [x] The app use javascript from front-end
- [x] The web app is mobile-responsive
- [x] Distinctiveness and Complexity
- [x] How to run the application
- [x] requirements.txt

## Recipes
![all recipes](https://res.cloudinary.com/dqxtoises/image/upload/v1640382187/recipes_jnxvnq.png)

You can see all the recipes added in the main page.

Recipe Inputs
- Title
- Ingredients
- Description
- Tags

The author of the recipes can edit the 
recipe.

The recipes can be filterd by author and tags.


## Day Menus
You can create a menu. The menu is composed
by  three recipes. one from breakfast, another 
for the meal and another for the dinner.


## Random
You can get a random recipe.
You can get a random day menu.
You can get a random week days.


## Body Fat Percentage
This page calculate:
  - Body Mass Index
  - Body Fat Percentage

Inputs:
  - Height (cm)
  - Weight (kg)
  - Age (years)
  - Gender 

## Shopping List
In this page you can add products on a list.
The product can be:
  - deleted
  - edited
  - checked

The list calculates the total price of all
articles

# Zone
This part of the app is for create menus with
the structure of the zone diet.

## Add Product
Add a product with this attributes:
- name
- price
- category (protein, carbs, fat)
- blocks 

## Create Menu
Crate a menu with the products of the zone
  - menu name
  - proteins product
  - carbs product
  - fats product

## Zone Menus
Show a list of cards when each card is menu.
each menu is divided by the three macronutrients.
and each macronutrient has his own color.
  - protein (red)
  - carb (green)
  - fat (yellow)

## Zone Day
This page can create a zone day when each day 
is composed by five menus:
  - Breakfast
  - Snack I
  - Meal 
  - Sanck II
  - Dinner

## Show Days
Here you can see all the days created,
each day is divided in five menus and each menus
has is own color:
  - breakfast ( yellow )
  - snack I ( blue )
  - meal ( green )
  - snack II (blue)
  - dinner ( dark )

# Distinctiveness and Complexity
  - This isn't a social network
  - This isn't a e-commerce
  - This isn't the pizza App
  - This platform is designed to help people to eat better
  - This app can save delicious recipes
  - This application use 7 models
  - Some models use ForeignKeys

# How to Run Application

`clone https://github.com/grayTurtle01/recipes.git`

`cd project `

`pip3 install -r requirements.txt`

`python3 manage.py runserver`

`localhost:8000`

