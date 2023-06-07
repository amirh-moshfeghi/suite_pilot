from django.contrib.auth.views import LogoutView
from django.urls import path
from Accounts import views

app_name = 'Account'

urlpatterns = (
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

)
