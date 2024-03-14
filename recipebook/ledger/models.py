from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=50)
    biography = models.TextField(
        # bio more than 255 characters
        validators=[MinLengthValidator(256)]
    )


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("ledger:ingredient", args=[str(self.name)])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name="recipe")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("ledger:recipe", args=[str(self.pk)])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        to=Ingredient, on_delete=models.CASCADE, related_name="recipe"
    )
    recipe = models.ForeignKey(
        to=Recipe, on_delete=models.CASCADE, related_name="ingredient"
    )
