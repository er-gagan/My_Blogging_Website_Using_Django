from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome),
    path('<str:slug>', views.blogPost),
]
