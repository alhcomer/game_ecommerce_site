from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("My gaming e-commerce platform index page")
