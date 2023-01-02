from django import forms
from .models import UserBase
from django_countries import widgets, countries
from phonenumber_field.formfields import PhoneNumberField

class RegistrationForm(forms.ModelForm):
    email = forms.CharField(
        label='Enter Email', min_length=5, max_length=100, help_text='Required', error_messages={'required': 'Please enter a valid email address'}
    )
    username = forms.CharField(
        label='Enter Username', min_length=5, max_length=20, help_text='Required'
    )
    first_name = forms.CharField(
        label="First Name", min_length=1,
        max_length=25, help_text='Required'
    )
    last_name = forms.CharField(
        label="Last Name", min_length=1,
        max_length=25, help_text='Required'
    )
    country = forms.ChoiceField(
        widget=widgets.CountrySelectWidget, choices=countries
    )
    # TODO: need to make phone number field show appropriate country code
    phone_number = PhoneNumberField()
    town_city = forms.CharField(label="City", min_length=2, max_length=100, help_text='Required')
    
