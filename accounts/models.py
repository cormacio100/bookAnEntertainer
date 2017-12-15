# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone


# Create your CUSTOM USER models here.
class AccountUserManager(UserManager):
    #   OVERRIDE THE DEFAULT create_user METHOD
    #def _create_user(self, username, email, password, first_name, last_name, location, is_entertainer, is_superuser, **extra_fields):
    def _create_user(self, username, email, password, first_name='generic',last_name='user',is_staff=0,is_superuser=0, **extra_fields):
        #   At this point the user is saved to the DB
        #   The code below allows you to change it's attributes

        """
        Creates and saves a User with the given username, email and password
        :param username:
        :param email:
        :param password:
        :param is_staff:
        :param is_supervisor:
        :param extra_fields:
        :return: user
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        #   Send to Parent class model
        user = self.model(username=email, email=email, first_name=first_name, last_name=last_name, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


#   CUSTOM USER CLASS
class User(AbstractUser):
    #   Now that we have abstracted this class we can add any number of custom attributes to our user class

    #   Replace the normal USER OBJECTS property with the custom AccountUserManager
    #   Overrides the default _create_user_method which normally checks for username. Instead we will check for email address
    #   Need to update settings.py to tell Django we want to use this class as our User Class
    #   E.G. AUTH_USER_MODEL = 'accounts.User'

    #   THE DEFAULT USER ATTRIBUTES ARE:
        #   USERNAME
        #   PASSWORD
        #   FIRST_NAME
        #   LAST_NAME
        #   EMAIL
        #   IS_SUPERUSER
        #   IS_ACTIVE
    #   Now that we've abstracted this class WE CAN ADD ANY NUMBER OF CUSTOM ATTRIBUTES TO OUR USER CLASS
    #   FIRST define the relevant form element in forms.py and then ADD THEM TO THE MODEL HERE
    account_type = models.CharField(max_length=11,default='General')

    #   Entertainers booked by the user
    booked_entertainers = models.CharField(max_length=255,default='No Bookings')
    objects = AccountUserManager()