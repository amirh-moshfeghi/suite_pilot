from django import forms
from tinymce.widgets import TinyMCE

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


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class CompanyForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفا نام شرکت را به فارسی وارد نمایید"})
        self.fields["english_title"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفا نام شرکت را به انگلیسی وارد نمایید"})
        self.fields["code"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفا کد شرکت را وارد نمایید"})
        self.fields["company_status"].widget.attrs.update({"class": "form-control form-control-solid"})
        self.fields["content"].widget.attrs.update({"class": "tox-target","id":"kt_docs_tinymce_basic", "name":"kt_docs_tinymce_basic","placeholder":"لطفا در صورت نیاز به ذخیره سازی داده های اضافی، اطلاعات یا فایل مورد نظر خود را در این قسمت وارد نمایید"})

    class Meta:
        model = Company
        fields = '__all__'


class DepartmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفا نام معاونت را به فارسی وارد نمایید"})
        self.fields["english_title"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفا نام معاونت را به انگلیسی وارد نمایید"})
        self.fields["code"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفا کد معاونت را وارد نمایید"})
        self.fields["department_status"].widget.attrs.update({"class": "form-control form-control-solid" })
        self.fields["department_type"].widget.attrs.update({"class": "form-control form-control-solid"})
        self.fields["order"].widget.attrs.update({"class": "form-control form-control-solid"})
        self.fields["company"].widget.attrs.update({"class": "form-control form-control-solid"})

    class Meta:
        model = Department
        fields = '__all__'


class OUForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفا نام واحد سازمانی را به فارسی وارد نمایید"})
        self.fields["english_title"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفانام واحد سازمانی را به انگلیسی وارد نمایید"})
        self.fields["code"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفا کد واحد سازمانی را وارد نمایید"})
        self.fields["ou_status"].widget.attrs.update({"class": "form-control form-control-solid" ,"placeholder":"لطفا وضعیت واحد سازمانی را وارد نمایید"})
        self.fields["order"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفا ترتیب واحد سازمانی را وارد نمایید"})
        self.fields["department"].widget.attrs.update({"class": "form-control form-control-solid","placeholder":"لطفا کد معاونت را انتخاب نمایید"})

    class Meta:
        model = OU
        fields = '__all__'