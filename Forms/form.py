from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from Forms.models import FormLetters


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FormLetters
        fields = '__all__'
