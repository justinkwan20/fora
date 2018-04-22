from django.urls import path
from . import views
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('new', views.new, name='new'),
    path('listings', views.index, name='index'),
    path('register', views.register, name='register'),
    path('log_in', views.login, name='log_in'),
    #Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls'))
]
