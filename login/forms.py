from django import forms
from .models import UserBase
from django_countries import widgets, countries
from phonenumber_field.formfields import PhoneNumberField

class RegistrationForm(forms.ModelForm):
    email = forms.CharField(
        label='Enter Email', min_length=5, max_length=100, help_text='Required', 
        error_messages={'required': 'Please enter a valid email address'}
    )
    username = forms.CharField(
        label='Enter Username', min_length=5, max_length=20,
        error_messages={'required': 'Please enter a username'}
    )
    first_name = forms.CharField(
        label="First Name", min_length=1,
        max_length=25,
        required=True,
        error_messages={'required': 'Please enter your first name'}
    )
    last_name = forms.CharField(
        label="Last Name", min_length=1,
        max_length=25, help_text='Required',
        error_messages={'required': 'Please enter a valid password'}
    )
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput,
        error_messages={'required': 'Please enter a matching password'}
        )
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput
        )
    country = forms.ChoiceField(label='Repeat Password', 
        widget=widgets.CountrySelectWidget, choices=countries,
        error_messages={'required': 'Please choose your country'}
        )
    phone_number = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': 'Phone Number'}),
        label="Phone Number", help_text='Required', 
        error_messages={'required': 'Please enter a valid phone number'}
        )
    town_city = forms.CharField(label="City", min_length=2, max_length=100, help_text='Required')

    class Meta:
        model = UserBase
        fields = ('username', 'email')
    
