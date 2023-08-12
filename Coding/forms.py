from django import forms
from .models import Child_Specs, Identity_Group

class Child_SpecsForm(forms.ModelForm):
    class Meta:
        model = Child_Specs
        fields = ('parent_name', 'parent_id', 'name', 'value')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].queryset = Identity_Group.objects.none()

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child_Specs
        fields = ('parent_name', 'parent_id', 'name', 'value')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].queryset = Identity_Group.objects.none()

        if 'parent_name' in self.data:
            try:
                parent_id = int(self.data.get('parent_name'))
                self.fields['value'].queryset = Identity_Group.objects.filter(parent_id=parent_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['value'].queryset = self.instance.parent_name.value_set.order_by('name')