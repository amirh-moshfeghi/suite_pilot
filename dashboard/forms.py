from django import forms
from .models import *


class ManagerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["persian_name"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفا نام مدیر را به فارسی وارد نمایید"})
        self.fields["english_name"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفانام مدیر را به انگلیسی وارد نمایید"})
        self.fields["code"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفا کد مدیر را وارد نمایید"})
        self.fields["order"].widget.attrs.update({"class": "form-control form-control-solid"})
        self.fields["manager_status"].widget.attrs.update({"class": "form-control form-control-solid"})

    class Meta:
        model = Manager
        fields = '__all__'

