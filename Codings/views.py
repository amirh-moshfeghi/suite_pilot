from django.shortcuts import render

from Accounts.models import AuditEntry
from dashboard.models import QuickLinks, SubMenu
from django.http import HttpResponse, JsonResponse, HttpRequest
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
#     return render(request, "Codings/Coding_New_Style.html",{'current_user_logs':current_user_logs,'quick_links':quick_links,'submenu':submenu})
#
#



# Create your views here.


def Coding_View(request, **kwargs):

    print(kwargs)

    if request.method == 'GET':

        form = RecipeForm()
        request_getdata = request.POST.get('getdata', None)
        # make sure that you serialise "request_getdata"
        print(JsonResponse(request_getdata,safe=False))
        return render(request, "Codings/Codings_New_Style.html", {'form': form})

    elif request.method == 'POST':
        form = RecipeForm(request.POST)
        request_getdata = request.POST.get('getdata', None)
        # make sure that you serialise "request_getdata"
        print(JsonResponse(request_getdata, safe=False))

        if form.is_valid():
            request_getdata = request.POST.get('getdata', None)
            # make sure that you serialise "request_getdata"
            print(JsonResponse(request_getdata))
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

            print(list(request.POST.items()))
        args = {'form': form, 'ingredients': ingredients, 'servingsizes': servingsizes, 'cooktimes': cooktimes,
                'recipes': recipes, 'directions': directions, 'cookwares': cookwares}

        return render(request, "Codings/Codings_New_Style.html", args)



