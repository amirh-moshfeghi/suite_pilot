from django import forms
from smart_selects.db_fields import ChainedForeignKey
from smart_selects.form_fields import ChainedModelChoiceField
from .models import Recipe, Direction, RecipeIngredient
from django.forms import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field


# pylint: disable=E1101

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('category', 'subcategory', 'recipename', 'child_specs_value')

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

        self.fields['category'].empty_label = 'Material_Group'
        self.fields['subcategory'].empty_label = 'Identity Group'
        self.fields['recipename'].empty_label = 'Child Specs'
        self.fields['child_specs_value'].empty_label = 'Values'