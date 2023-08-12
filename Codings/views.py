from django.shortcuts import render

from Accounts.models import AuditEntry
from dashboard.models import QuickLinks, SubMenu
from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe, RecipeName, RecipeIngredient, Direction, Cookware, RecipeCookware, Image, CookTime, \
    ServingSize, Ingredient
from django.views.generic import View
from .forms import RecipeForm
from django.forms import widgets


# def home(request):
#     current_user_username=request.user.username
#     current_user_logs = AuditEntry.objects.filter(username=current_user_username)
#     quick_links = QuickLinks.objects.all()
#     submenu = SubMenu.objects.all()
#
#
#     # g = GeoIP2()
#
#     print(current_user_logs[0].ip)
#     return render(request, "Codings/Codings_New_Style.html",{'current_user_logs':current_user_logs,'quick_links':quick_links,'submenu':submenu})
#
#



# Create your views here.
class recipe_view(View):

    def get(self, request):
        form = RecipeForm()
        return render(request, "Codings/Codings_New_Style.html", {'form': form})

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            tex = form.cleaned_data['recipename'].id
            recipes = Recipe.objects.filter(recipename_id=tex).values('id', 'category__category',
                                                                      'subcategory__subcategory',
                                                                      'recipename__recipename'
                                                                      ,'child_specs_value__child_specs_value', 'image', 'description')
            ingredients = RecipeIngredient.objects.filter(recipe__in=recipes.values('id'))
            directions = Direction.objects.filter(recipe__in=recipes.values('id'))
            cookwares = RecipeCookware.objects.filter(recipe__in=recipes.values('id'))
            cooktimes = CookTime.objects.filter(recipe__in=recipes.values('id'))
            servingsizes = ServingSize.objects.filter(recipe__in=recipes.values('id'))
        args = {'form': form, 'ingredients': ingredients, 'servingsizes': servingsizes, 'cooktimes': cooktimes,
                'recipes': recipes, 'directions': directions, 'cookwares': cookwares}
        return render(request, "Codings/Codings_New_Style.html", args)