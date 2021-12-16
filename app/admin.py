from django.contrib import admin
from app.models import User, Recipe, DayMenu, Product

# Register your models here.
admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(DayMenu)
admin.site.register(Product)