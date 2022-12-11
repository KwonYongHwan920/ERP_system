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
path('proSins', views.proS_ins),
path('tb_ins', views.tb_ins),
path('comm_ins', views.comm_ins),
path('br_ins', views.br_ins),
path('staff_ins', views.staff_ins),
path('client_ins', views.client_ins),
path('prosmanage', views.pros_manage),
]