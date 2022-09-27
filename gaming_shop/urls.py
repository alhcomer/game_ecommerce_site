from argparse import Namespace
from xml.etree.ElementInclude import include
from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
]
