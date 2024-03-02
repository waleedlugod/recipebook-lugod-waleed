from django.shortcuts import render

from ledger.models import Ingredient, Recipe


def recipe_list(request):
    recipe_list = {"recipe_list": Recipe.objects.all()}
    return render(request, "recipe_list.html", recipe_list)


def recipe1(request):
    recipe = {
        "name": "Recipe 1",
        "ingredients": [
            {"name": "tomato", "quantity": "3pcs"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "pork", "quantity": "1kg"},
            {"name": "water", "quantity": "1L"},
            {"name": "sinigang mix", "quantity": "1 packet"},
        ],
        "link": "/recipe/1",
    }
    return render(request, "recipe_ingredients.html", recipe)


def recipe2(request):
    recipe = {
        "name": "Recipe 2",
        "ingredients": [
            {"name": "garlic", "quantity": "1 head"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "vinegar", "quantity": "1/2cup"},
            {"name": "water", "quanity": "1 cup"},
            {"name": "salt", "quantity": "1 tablespoon"},
            {"name": "whole black peppers", "quantity": "1 tablespoon"},
            {"name": "pork", "quantity": "1 kilo"},
        ],
        "link": "/recipe/2",
    }
    return render(request, "recipe_ingredients.html", recipe)
