from django.contrib import admin
from smart_selects.db_fields import ChainedForeignKey

# Register your models here.
from .models import Ingredient, Recipe, Category, Direction, Image, Subcategory, Amount, Unit, RecipeIngredient, \
    RecipeName, RecipeCookware, Cookware, CookTime, Hour, Minute, ServingSize, ChildSpecsValue


class CategoryAdmin(admin.ModelAdmin):
    ordering = ('category',)
    pass


admin.site.register(Category, CategoryAdmin)


class ChildSpecsValueAdmin(admin.ModelAdmin):
    ordering = ('child_specs_value',)
    pass


admin.site.register(ChildSpecsValue, ChildSpecsValueAdmin)

# class AmountAdmin(admin.ModelAdmin):
#     ordering = ('amount',)
#     pass
#
#
# admin.site.register(Amount, AmountAdmin)


# class UnitAdmin(admin.ModelAdmin):
#     ordering = ('unit',)
#     pass
#
#
# admin.site.register(Unit, UnitAdmin)


class SubcategoryAdmin(admin.ModelAdmin):
    ordering = ('subcategory',)
    pass


admin.site.register(Subcategory, SubcategoryAdmin)


class RecipeNameAdmin(admin.ModelAdmin):
    ordering = ('recipename',)
    pass


admin.site.register(RecipeName, RecipeNameAdmin)


# class ImageAdmin(admin.ModelAdmin):
#     ordering = ('image_title',)
#     pass
#
#
# admin.site.register(Image, ImageAdmin)


# class IngredientAdmin(admin.ModelAdmin):
#     ordering = ('ingredient',)
#     pass
#
#
# admin.site.register(Ingredient, IngredientAdmin)


# class RecipeCookwareAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(RecipeCookware, RecipeCookwareAdmin)


# class CookwareAdmin(admin.ModelAdmin):
#     ordering = ('cookware',)
#     pass
#
#
# admin.site.register(Cookware, CookwareAdmin)


# class CookTimeAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(CookTime, CookTimeAdmin)


# class HourAdmin(admin.ModelAdmin):
#     ordering = ('hour',)
#     pass
#
#
# admin.site.register(Hour, HourAdmin)


# class MinuteAdmin(admin.ModelAdmin):
#     ordering = ('minute',)
#     pass


# admin.site.register(Minute, MinuteAdmin)
#
#
# class ServingSizeAdmin(admin.ModelAdmin):
#     ordering = ('servingsize',)
#     pass
#
#
# admin.site.register(ServingSize, ServingSizeAdmin)


# INLINES

# class RecipeCookwareInLine(admin.TabularInline):
#     model = RecipeCookware
#     extra = 0
#
#
# class RecipeIngredientInline(admin.TabularInline):
#     model = RecipeIngredient
#     extra = 0
#
#
# class DirectionInLine(admin.TabularInline):
#     model = Direction
#     extra = 0
#

# ADMIN Interface

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['category']}),
        (None, {'fields': ['subcategory']}),
        (None, {'fields': ['recipename']}),
        (None, {'fields': ['image']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['cooktime']}),
        (None, {'fields': ['servingsize']})
    ]
    # inlines = [RecipeCookwareInLine, RecipeIngredientInline, DirectionInLine]


admin.site.register(Recipe, RecipeAdmin)