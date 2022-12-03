from django.shortcuts import render

def login(request):
    return render(request, 'gaming_shop/login.html')

def sign_up(request):
    return render(request, 'gaming_shop/sign-up.html')