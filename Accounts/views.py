from django.shortcuts import render
from django.urls import reverse_lazy

from Accounts.decorators import is_login
from Accounts.models import User
from django.contrib import (
    auth,
    messages,
)
from django.shortcuts import (
    render,
    redirect,
)


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        print("yes")
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
            return redirect(reverse_lazy('home'))

        else:
            messages.error(request, 'نام کاربری یا گذرواژه وارد شده نادرست است')
    context = {
        'page_title': 'ورود',
    }
    return render(request, "dashboard/sign-in.html", context)