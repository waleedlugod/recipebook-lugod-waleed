from django.shortcuts import render
from ledger.models import Ingredient, Recipe, RecipeIngredient


def recipe_list(request):
    recipe_list = {"recipe_list": Recipe.objects.all()}
    return render(request, "recipe_list.html", recipe_list)


def recipe_detail(request, id):
    recipe_name = Recipe.objects.get(pk=id)
    recipe_detail = {
        "ingredients": RecipeIngredient.objects.filter(recipe__name=recipe_name)
    }
    return render(request, "recipe_detail.html", recipe_detail)
