from django.urls import path

from .views import recipe_list, recipe1, recipe2

urlpatterns = [
    path("recipes/list", recipe_list, name="recipe_list"),
    path("recipe/<int:id>", recipe1, name="recipe"),
]

app_name = "ledger"
