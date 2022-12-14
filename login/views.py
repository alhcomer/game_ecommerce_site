from django.shortcuts import render, redirect
from .forms import RegistrationForm
from phonenumber_field.phonenumber import PhoneNumber
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from .token_generator import account_activation_token
from django.http import HttpResponse


def login(request):
    return render(request, 'login/login.html')

def sign_up(request):
    #TODO add google sign_up/login


    # if request.user.is_authenticated:
    #     return redirect('/')
        #TODO: redirect to user dashboard after creations instead of home page
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            user.email = registration_form.cleaned_data['email']
            user.first_name = registration_form.cleaned_data['first_name']
            user.last_name = registration_form.cleaned_data['last_name']
            user.set_password(registration_form.cleaned_data['password'])
            user.country = registration_form.cleaned_data['country']
            user.date_of_birth = registration_form.cleaned_data['date_of_birth']
            user.phone_number = registration_form.cleaned_data['phone_number']
            user.town_city = registration_form.cleaned_data['town_city']
            user.is_active = False
            user.save()
            # Set up email
            #TODO: need to set up send email
            #TODO: need to add phone number validation
            #TODO: need to add password strength checker

            current_site = get_current_site(request)
            subject = 'Activate your Account'  
            message = render_to_string(
                'login/registration/account-activation-email.html',
                {
                'user': user,
                'domain': current_site.domain,
                'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                })
            user.email_user(subject=subject, message=message, registrant=user)
            render(request, 'login/registration/authenticate-message.html')
        else:
            print(registration_form.errors.as_data())
        return render(request, 'login/registration/sign-up.html', {'form': registration_form})

    else:
        registration_form = RegistrationForm()
        return render(request, 'login/registration/sign-up.html', {'form': registration_form})

def authenticate(request):
    return render(request, 'login/registration/authenticate-message.html')