

from django.urls import path

from . import views

app_name = "resume"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('languages/', views.languages, name='languages'),
    path('services/', views.services, name='services'),
    path('contact/', views.contacts, name='contact'),


]