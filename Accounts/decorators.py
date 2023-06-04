from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy


def is_login():
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if request.user.is_anonymous:
              return view_func(request, *args, **kwargs)
            if request.user.is_superuser or request.user.is_manager:
                return redirect(reverse_lazy('home'))

        return wrap

    return decorator
