from django.urls import path

from Stickynotes import views

urlpatterns = [
    path("", views.BookinWizardView.as_view(), name="index"),

]