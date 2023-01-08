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
        label="Date of Birth", widget=forms.SelectDateWidget,
        error_messages={'required': 'Please enter a matching password.'}
    )
    country = forms.ChoiceField(label='Country of Residence', 
        widget=widgets.CountrySelectWidget, choices=countries,
        error_messages={'required': 'Please choose your country.'}
        )
        # TODO: need to finish phone number widget validation
        # https://django-phonenumber-field.readthedocs.io/en/latest/reference.html#widgets

    town_city = forms.CharField(
        label="town/city", min_length=2,
        max_length=40
    )    
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

    def clean_email(self):
        email = self.cleaned_data['email']
        r = UserBase.objects.filter(email=email)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return email

    def password2_check(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def send_activation_email():
        pass
    # maybe delete

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3'}
        )
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-3'}
        )
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control mb-3'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control mb-3'}
        )
        #TODO: Finish adding attributes to widgets
        #TODO: Need to add CSS styling that works with bootstrap for the forms


class LoginForm(forms.ModelForm):
    pass
    
