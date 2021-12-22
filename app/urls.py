from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_recipe", views.add_recipe, name="add_recipe"),
    path("filter_by_tag/<str:tag>", views.filter_by_tag, name="filter_by_tag"),
    path("edit_recipe/<int:recipe_id>", views.edit_recipe, name="edit_recipe"),
    path("profile/<str:user_id>", views.profile, name="profile"),
    path("recipe/<int:recipe_id>", views.recipe, name="recipe"),
    path("add_menu", views.add_menu, name="add_menu"),
    path("show_menus", views.show_menus, name="show_menus"),
    path("edit_menu/<int:menu_id>", views.edit_menu, name="edit_menu"),
    path("random_recipe", views.random_recipe, name="random_recipe"),
    path("random_menu", views.random_menu, name="random_menu"),
    path("random_week", views.random_week, name="random_week"),
    path("get_fat", views.get_fat, name="get_fat"),
    path("shopping_list", views.shopping_list, name="shopping_list"),
    path("add_product", views.add_product, name="add_product"),
    path("delete_product/<int:product_id>", views.delete_product, name="delete_product"),
    path("check_uncheck/<int:product_id>", views.check_uncheck, name="check_uncheck"),
    path("update_product", views.update_product, name="update_product"),
    path("zone_add_product", views.zone_add_product, name="zone_add_product"),
    path("zone_create_menu", views.zone_create_menu, name="zone_create_menu"),
    path("zone_menus", views.zone_menus, name="zone_menus"),
    path("zone_menu/<int:menu_id>", views.zone_menu, name="zone_menu"),
    path("zone_create_day", views.zone_create_day, name="zone_create_day"),
    path("zone_days", views.zone_days, name="zone_days"),
]
