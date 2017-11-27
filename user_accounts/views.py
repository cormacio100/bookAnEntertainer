# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import json

# Create your views here.


def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            password = request.POST['password1']
            #   CREATE A USER ACCOUNT
            User.objects.create_user(username=username, password=password)
                #   forward user to next choice
            #   THEN RETRIEVE THE USER ID FOR THE NEW ACCOUNT
            user_account_id = User.objects.get(username=username).id
            print('user_account_id is:  '+str(user_account_id))
            args = {'account_id': User.objects.get(username=username).id}

            return redirect(reverse('registration_type'))
        else:
            args = {'error': '**Passwords do not match**'}
            return render(request,'user_accounts/register.html',args)
    else:
        #   INITIAL LOAD
        return render(request, 'user_accounts/register.html')


def registration_type(request):
    return render(request, 'user_accounts/registered_user_type.html')