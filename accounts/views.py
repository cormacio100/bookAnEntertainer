# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from accounts.models import User

# VIEW TO DISPLAY REGISTER FORM
def auth_register(request):
    #   ONCE THE REGISTRATION FORM IS SUBMITTED
    if request.method == 'POST':
        #   check that the ass
        if request.POST['password1']==request.POST['password2']:

            try:
                user = User.objects.get(username=request.POST['email'])
                messages.error(request, "Username Already Exists")
                return redirect(reverse('accounts:register'))
            except User.DoesNotExist:

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
        else:
            messages.error(request, "Passwords do not Match")
            return redirect(reverse('accounts:register'))
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

                messages.success(request,"Logged in as: "+user.email)
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
    #args = {'last_login': request.user.last_login}

    ##################################################################################################################
    #   -   Retrieve the relevant user
    #   -   Extract the string containing list of booked entertainers
    #   -   Convert the string into a list of objects
    #   -   Display in view
    ##################################################################################################################
    user_id = request.session['_auth_user_id']
    user = User.objects.get(pk=user_id)

    booked_entertainers = user.booked_entertainers

    booked_entertainers_list = booked_entertainers.split(",")

    return render(request, 'accounts/profile.html')