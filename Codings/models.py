from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Minute(models.Model):
    minute = models.CharField(max_length=250)

    def __str__(self):
        return self.minute


class Hour(models.Model):
    hour = models.CharField(max_length=250)

    def __str__(self):
        return self.hour


class CookTime(models.Model):
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE)
    minute = models.ForeignKey(Minute, on_delete=models.CASCADE)

    # pylint: disable=E1101
    def __str__(self):
        return self.hour.hour + " hr and " + self.minute.minute + " min"
    # pylint: enable=E1101


class ServingSize(models.Model):
    servingsize = models.CharField(max_length=250)

    def __str__(self):
        return self.servingsize


class Image(models.Model):
    image_title = models.CharField(max_length=250, default=None, blank=True, null=True)
    image = models.ImageField(upload_to='images/', default=None, blank=True, null=True)

    def __str__(self):
        return self.image_title


class Amount(models.Model):
    amount = models.CharField(max_length=250)

    def __str__(self):
        return self.amount


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=250)
    link = models.CharField(max_length=250, default=None, blank=True, null=True)
    image = models.ImageField(upload_to='images/', default=None, blank=True, null=True)

    def __str__(self):
        return self.ingredient


class Unit(models.Model):
    unit = models.CharField(max_length=250)

    def __str__(self):
        return self.unit


class Category(models.Model):
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.category


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.subcategory


class RecipeName(models.Model):
    # description = models.TextField(default="")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    recipename = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.recipename


class ChildSpecsValue(models.Model):
    # description = models.TextField(default="")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    recipename = models.ForeignKey(RecipeName, on_delete=models.CASCADE, null=True)
    child_specs_value = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.child_specs_value


class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = ChainedForeignKey(
        Subcategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=False,
        sort=True
    )
    recipename = ChainedForeignKey(
        RecipeName,
        chained_field="subcategory",
        chained_model_field="subcategory",
        show_all=False,
        auto_choose=False,
        sort=True
    )
    child_specs_value = ChainedForeignKey(
        ChildSpecsValue,
        chained_field="recipename",
        chained_model_field="recipename",
        show_all=False,
        auto_choose=False,
        sort=True,
        null=True

    )
    image = models.TextField(default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    cooktime = models.ForeignKey(CookTime, on_delete=models.CASCADE, default=None, blank=True, null=True)
    servingsize = models.ForeignKey(ServingSize, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        # pylint: disable=E1101
        return self.recipename.recipename
        # pylint: enable=E1101


class RecipeIngredient(models.Model):
    # image = models.ForeignKey(Image, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.ForeignKey(Amount, on_delete=models.CASCADE, default=None, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        # pylint: disable=E1101
        return self.ingredient.ingredient
        # pylint: enable=E1101


class Direction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    directions = models.TextField()

    def __str__(self):
        return self.directions


class Cookware(models.Model):
    cookware = models.CharField(max_length=250)
    link = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.cookware


class RecipeCookware(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    cookware = models.ForeignKey(Cookware, on_delete=models.CASCADE)

    def __str__(self):
        # pylint: disable=E1101
        return self.cookware.cookware
        # pylint: enable=E1101


