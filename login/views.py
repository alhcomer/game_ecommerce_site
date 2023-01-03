from django.shortcuts import render, redirect
from .forms import RegistrationForm

def login(request):
    return render(request, 'login/login.html')

def sign_up(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
        #TODO: redirect to user dashboard after creations instead of home page
    if request.method == 'GET':
        return render(request, 'login/sign-up.html')
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            user.username = registration_form.cleaned_data['username']
            user.email = registration_form.cleaned_data['email']
            user.first_name = registration_form.cleaned_data['first_name']
            user.last_name = registration_form.cleaned_data['last_name']
            user.set_password(registration_form.cleaned_data['password'])
            user.country = registration_form.cleaned_data['country']
            user.phone_number = registration_form.cleaned_data['phone_number']
            user.town_city = registration_form.cleaned_data['town_city']
            user.is_active = False
            user.save()
            return redirect('authenticate')

def authenticate(request):
    return render(request, 'login/authenticate-sign-up.html')