# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def register(request):
    if request.method == 'POST':
        #   IF THE PASSWORDS MATCH
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            password = request.POST['password1']
            #   CHECK IF USERNAME ALREADY EXISTS, IF NOT, THEN CREATE A NEW USER AND LOG THEM IN
            try:
                user = User.objects.get(username=username)
                return render(request,'user_accounts/register.html',{'error':'Username already in use'})
            except:
                user = User.objects.create_user(username=username,password=password)
                login(request, user)
                args = {'error': 'Account created and logged in'}
                return redirect(request,'user_accounts/register.html', args)
        else:
            args = {'error': '**Passwords do not match**'}
            return render(request,'user_accounts/register.html',args)
    else:
        #   INITIAL LOAD
        return render(request, 'user_accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        #   IF THE USER EXISTS, LOG THEM IN, IF NOT DISPLAY AN ERROR
        if user is not None:
            login(request,user)
            args = {'error':'Logged in successfully'}
            return render(request,'user_accounts/login.html',args)
        else:
            args = {'error':'User not found'}
            return render(request,'user_accounts/login.html',args)
    else:
        #   WHEN PAGE LOADS INITIALLY
        return render(request,'user_accounts/login.html')


def registration_type(request):
    return render(request, 'user_accounts/registered_user_type.html')