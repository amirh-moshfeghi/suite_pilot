from django.shortcuts import render
from django.urls import reverse_lazy

from Accounts.decorators import is_login
from Accounts.models import User, AuditEntry
from django.contrib import (
    auth,
    messages,
)
from django.shortcuts import (
    render,
    redirect,
)

from dashboard.models import QuickLinks, SubMenu


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        try:
            username = request.POST['username']
        except User.DoesNotExist:
            messages.error(request, 'نام کاربری یا گذرواژه وارد شده نادرست است')

        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse_lazy('Dashboard:home'))

        else:
            messages.error(request, 'نام کاربری یا گذرواژه وارد شده نادرست است')
    context = {
        'page_title': 'ورود',
    }
    return render(request, "dashboard/sign-in.html", context)


def profile_logs(request):
    current_user_username=request.user.username
    current_user_logs = AuditEntry.objects.filter(username=current_user_username)
    quick_links = QuickLinks.objects.all()
    submenu = SubMenu.objects.all()


    # g = GeoIP2()

    print(current_user_logs[0].ip)
    return render(request, "dashboard/profile_logs.html",{'current_user_logs':current_user_logs,'quick_links':quick_links,'submenu':submenu})
