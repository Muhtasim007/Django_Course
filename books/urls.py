from django.contrib import admin
from django.urls import path
from . import views
from books.views import MyView, BookListView, ContactFormView 
from django.shortcuts import render

urlpatterns = [
path('initial_class/',MyView.as_view()),
path('list/',BookListView.as_view()),
path('contact/add/',ContactFormView.as_view()),
path('contact/success/', lambda request: render(request, 'success/contact_success.html'), name = 'contact_success'),
path('test/',views.test),
# path('', views.home,name="home"),
]