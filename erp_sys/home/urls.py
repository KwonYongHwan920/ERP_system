from django.contrib import admin
from django.urls import path
from home import views


# app_name = 'home'

urlpatterns = [
path(' ', views.welcome_home, name='welcome_home'),
]