from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import Child_SpecsForm
from .models import Child_Specs, Identity_Group


class Child_SpecsListView(ListView):
    model = Child_Specs
    form_class = Child_SpecsForm
    context_object_name = 'Child_Specs'

class Child_SpecsCreateView(CreateView):
    model = Child_Specs

    fields = ('parent_name', 'parent_id', 'name', 'value')
    success_url = reverse_lazy('Child_Specs_changelist')

class Child_SpecsUpdateView(UpdateView):
    model = Child_Specs
    form_class = Child_SpecsForm
    fields = ('parent_name', 'parent_id', 'name', 'value')
    success_url = reverse_lazy('Child_Specs_changelist')

def load_values(request):
    country_id = request.GET.get('country')
    values = Identity_Group.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'Coding/value_dropdown_list_options.html', {'values': values})