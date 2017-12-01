# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone


# Create your CUSTOM USER models here.
class AccountUserManager(UserManager):
    #   OVERRIDE THE DEFAULT create_user METHOD
    #def _create_user(self, username, email, password, first_name, last_name, location, is_entertainer, is_superuser, **extra_fields):
    def _create_user(self, username, email, password, is_superuser, **extra_fields):
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
        user = self.model(username=email, email=email, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


#   CUSTOM USER CLASS
class User(AbstractUser):
    #   Abstracting this class allows us to add any number of custom attributes to our user class

    #   Replace the normal USER OBJECTS property with the custom AccountUserManager
    #   Overrides the _create_user method
    #   Default version checks for username but we will check for email
    #   Need to update settings.py to tell Django we want to use this class as our User class
    #   AUTH_USER_MODEL = 'accounts.User'
    objects = AccountUserManager()
