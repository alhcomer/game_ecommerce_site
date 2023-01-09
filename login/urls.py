from xml.etree.ElementInclude import include
from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_up/<slug:uidb64>/<slug:token>)/', views.authenticate, name='authenticate')
]