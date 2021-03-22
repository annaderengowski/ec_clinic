from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_list, name='stock_list'),
    path('inventory/list', views.stock_list, name='stock_list'),
    path('inventory/add', views.add_donation, name='add_donation'),
    path('inventory/dispense', views.dispense, name='dispense'),
]
