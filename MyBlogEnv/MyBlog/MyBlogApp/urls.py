from django.urls import path
from . import views

urlpatterns = [
    path('postComment', views.postComment),
    path('', views.blogHome),
    path('<str:slug>', views.blogPost),
]