from xml.etree.ElementInclude import include
from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up')
]