from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("sedan", views.sedan, name="sedan"),
    path("hatchback", views.hatchback, name="hatchback"),
    path("suv", views.suv, name="suv"),
    path("supercar", views.supercar, name="supercar")
]