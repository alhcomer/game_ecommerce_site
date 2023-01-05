from django import forms
from .models import UserBase
from django_countries import widgets, countries
from phonenumber_field.formfields import PhoneNumberField
from django.forms.widgets import DateInput
from phonenumber_field.widgets import PhoneNumberPrefixWidget



class RegistrationForm(forms.ModelForm):
    email = forms.CharField(
        label='Enter Email', min_length=5, max_length=100, help_text='Required', 
        error_messages={'required': 'Please enter a valid email address.'}
    )
    first_name = forms.CharField(
        label="First Name", min_length=1,
        max_length=25,
        required=True,
        error_messages={'required': 'Please enter your first name.'}
    )
    last_name = forms.CharField(
        label="Last Name", min_length=1,
        max_length=25, help_text='Required',
        error_messages={'required': 'Please enter a valid password.'}
    )
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput,
        error_messages={'required': 'Please enter a matching password.'}
        )
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput,
        error_messages={'required': 'Please enter a matching password.'}
        )
    date_of_birth = forms.DateField(
        label="Date of Birth", widget=forms.DateInput,
        error_messages={'required': 'Please enter a matching password.'}
    )
    country = forms.ChoiceField(label='Repeat Password', 
        widget=widgets.CountrySelectWidget, choices=countries,
        error_messages={'required': 'Please choose your country.'}
        )
        # TODO: need to finish phone number widget validation
        # https://django-phonenumber-field.readthedocs.io/en/latest/reference.html#widgets
    phone_number = PhoneNumberField(
        label="Phone Number",
        widget=PhoneNumberPrefixWidget(   
            )
        )
    phone_number.error_messages['invalid'] = 'Invalid Mobile Number'
    town_city = forms.CharField(label="City", min_length=2, max_length=100, help_text='Required')
    terms = forms.BooleanField(
        label="I have read and agree to the terms and conditions.",
        error_messages={'required': 'Agreeing to terms and conditions is required for account creation.'})

    class Meta:
        model = UserBase
        fields = '__all__'

        widgets = {
            'date_of_birth': DateInput()
        }

class LoginForm(forms.ModelForm):
    pass
    
