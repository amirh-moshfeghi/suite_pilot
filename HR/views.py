import csv
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse

from HR.forms import ManagerForm
from HR.models import Manager


def Base_information_Manager(request):
    if request.method == "POST":
        manager_form = ManagerForm(request.POST, request.FILES)
        if manager_form.is_valid():
            manager_form.save()
            messages.success(request,'ثبت مدیر با موفقیت انجام شد')
        else:
            messages.error(request, 'مشکلی در ورودی اطلاعات.لطفا مجدد تلاش کنید')

        return redirect("Base_information_Manager")
    manager_form = ManagerForm()
    managers = Manager.objects.all()
    return render(request=request, template_name="HR/Base_Information.html", context={'manager_form': manager_form, 'managers': managers})

def export_managers_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="managers.csv"'
    response.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(response)
    writer.writerow(['id','persian_name', 'english_name', 'code', 'order', 'manager_status', 'queue_id', 'headquarter_id'])

    managers = Manager.objects.all().values_list('id','persian_name', 'english_name', 'code', 'order', 'manager_status', 'queue_id', 'headquarter_id')
    for manager in managers:
        writer.writerow(manager)

    return response


def delete_manager(request, id):
    manager = Manager.objects.get(id=id)
    manager.delete()
    return HttpResponseRedirect(reverse('Base_information_Manager'))


def update_manager(request, id):
    manager = Manager.objects.get(id=id)
    template = loader.get_template('HR/Base_Information_Manager_Update.html')
    context = {
        'manager': manager,
    }
    return HttpResponse(template.render(context, request))


def update_manager_record(request, id):
      persian_name = request.POST['persian_name']
      code = request.POST['code']
      english_name = request.POST['english_name']
      order = request.POST['order']
      manager_status = request.POST['manager_status']
      manager = Manager.objects.get(id=id)
      manager.persian_name = persian_name
      manager.english_name = english_name
      manager.code = code
      manager.order = order
      manager.manager_status = manager_status

      manager.save()
      return HttpResponseRedirect(reverse('create_hr_manager'))