from argparse import Namespace
from xml.etree.ElementInclude import include
from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('games/<slug:slug>', views.product_item, name='product_item'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('login/', views.login, name='login')
]
