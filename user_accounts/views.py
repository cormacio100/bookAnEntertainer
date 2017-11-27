# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            #   CREATE A USER ACCOUNT
            try:
                User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                #   forward user to next choice
                return render(request, 'user_accounts/registered_user_type.html')
            except:
                args = {'error': '**Username already exists**'}
                return render(request, 'user_accounts/register.html', args)
        else:
            args = {'error': '**Passwords do not match**'}
            return render(request,'user_accounts/register.html',args)
    else:
        #   INITIAL LOAD
        return render(request, 'user_accounts/register.html')

