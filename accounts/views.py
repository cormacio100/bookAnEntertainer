# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# VIEW TO DISPLAY REGISTER FORM
def auth_register(request):
    #   ONCE THE REGISTRATION FORM IS SUBMITTED
    if request.method == 'POST':
        #   retrieve values from CUSTOM FORM
        form = UserRegistrationForm(request.POST)
        #   save the form if it is valid
        if form.is_valid():
            form.save()
            #   AUTHENTICATE THE USER BASED ON EMAIL AND PASSWORD PASSED IN
            #   using authentication defined in function in backends.py file
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))
            #   Log the user in and show their profile
            if user:
                login(request,user)
                #   Check user_type the new user is
                if request.POST.get('account_type') == 'Entertainer':
                    #messages.success(request, "You have successfully registered as an Entertainer")
                    return redirect(reverse('entertainers:create_profile'))
                else:
                    messages.success(request, "You have successfully registered as a General User")
                return redirect(reverse('accounts:profile'))
            else:
                messages.error(request, "unable to log you in at this time!")

    #   INITIALLY THE METHOD WILL NOT BE EQUAL TO POST SO WILL DISPLAY THE EMPTY FORM
    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'accounts/register.html', args)


def auth_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        #   if the form is valid lg the user in and return user object
        if form.is_valid():
            #   check if user is authentic
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))
            #    if yes, log them in
            if user is not None:
                auth.login(request, user)
                request.user.last_login = user.last_login
                messages.error(request,"You have successfully logged in")
                return redirect(reverse('accounts:profile'))
            else:
                form.add_error(None,"Your email or password was not recognised")
    else:
        #   display empty form
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'accounts/login.html', args)


def auth_logout(request):
    auth.logout(request)
    messages.success(request,'You have successfully logged out')
    return redirect(reverse('home'))


@login_required(login_url='/login/')
def auth_profile(request):
    #   retrieve the user

    args = {'message': 'Profile loaded', 'last_login': request.user.last_login}
    return render(request, 'accounts/profile.html', args)