from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("ingredient", args=[str(self.name)])


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("recipe", args=[str(self.name)])


class RecipeIngredient(models.Model):
    quantity = models.DecimalField(max_digits=3, decimal_places=2)
    ingredient = models.ForeignKey(to=Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE)
