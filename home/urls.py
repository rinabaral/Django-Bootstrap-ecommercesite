from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name = 'index_page'),
    path('contact', views.contact_page, name = 'contact_page'),
    path('category', views.category_page, name = 'category_page'),
    path('about', views.about_page, name = 'about_page'),
]
