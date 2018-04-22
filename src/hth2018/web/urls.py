from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new', views.new, name='new'),
    path('listings', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login')
]
