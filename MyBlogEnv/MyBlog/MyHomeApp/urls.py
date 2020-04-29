from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contact', views.contact),
    path('about', views.about),
    path('search', views.search),
    path('signup', views.handleSignup),
    path('login', views.handleLogin),
    path('logout', views.handleLogout),
]
