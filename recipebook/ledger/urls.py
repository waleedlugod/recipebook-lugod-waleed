from django.urls import path

from .views import recipe_detail, recipe_list

urlpatterns = [
    path("recipes/list", recipe_list, name="recipe_list"),
    path("recipe/<int:id>", recipe_detail, name="recipe"),
]

app_name = "ledger"
