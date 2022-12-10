from django.contrib import admin
from django.urls import path
from home import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
path('', views.welcome_home, name='welcome_home'),
# fixme : 로그인 기능 만들기
# path('logIn', views.logIn),
path('tbList', views.tbList),
path('proins', views.pro_ins),
path('finance', views.finance),
path('product', views.pro_view),
path('product_s', views.proS_view),
path('sales', views.sales_view),
path('staff', views.staff_view),
path('clients', views.clients_view),
]