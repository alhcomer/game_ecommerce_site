from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.mail import send_mail
import os

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser = True'
            )
        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address.'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserBase(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    country = CountryField()
    date_of_birth = models.DateField(max_length=8)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    town_city = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name',
                        'last_name', 'country', 'phone_number', 
                        'date_of_birth', 'town_city',]


    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.email

    def email_user(self, subject, message, registrant):
        send_mail(
            subject=subject,
            message=message,
            recipient_list=[str(registrant), ],
            from_email=os.getenv('EMAIL_ADDRESS'),
            auth_user=os.getenv('EMAIL_ADDRESS'),
            auth_password=os.getenv('EMAIL_PASSWORD'),
            fail_silently=False,
        )