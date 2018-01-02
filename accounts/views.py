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
from entertainers.models import Entertainer

##########################################
#   LOGGING
##########################################
import logging
log = logging.getLogger(__name__)

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

                            ######
                            #   IF AN ENTERTAINER SET THE USER.IS_STAF VALUE TO 1
                            #
                            #######

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
    #   -   Check what type of user they are
    #       -   If Entertainer need to retrieve the associated Entertainer ID
    #   -   Extract the string containing list of booked entertainers
    #   -   Convert the string into a list of objects
    #   -   Display in view
    ##################################################################################################################
    user_id = request.session['_auth_user_id']
    user = User.objects.get(pk=user_id)

    account_type_entertainer = False
    associated_entertainer = {}
    message = ''

    if 'Entertainer' == user.account_type:
        account_type_entertainer = True
        #   retrieve the entertainer associated with the user
        associated_entertainer = Entertainer.objects.get(user_id=user_id)

    messages.success(request,'Logged in as: '+user.username)

    #   retrieve string of booked entertainers
    booked_entertainers = user.booked_entertainers
    #message = 'string is '+booked_entertainers

    bookings_made = False

    if booked_entertainers == 'No Bookings':
        #account_type_entertainer = False
        args = {'account_type_entertainer': account_type_entertainer,'bookings_made':bookings_made,'associated_entertainer':associated_entertainer,'message':message}
        return render(request, 'accounts/profile.html', args)
    else:
        bookings_made = True
        if len(booked_entertainers) == 1:
            booked_entertainers_list = int(booked_entertainers)
        else:
            #   remove the last comma
            booked_entertainers = booked_entertainers.rstrip(',')
            #   then split the string into a list of strings based on the diving comma
            booked_entertainers_list = booked_entertainers.split(",")
        #comma_list = []
        entertainer_id_list =[] #   contains list of IDs
        #date_list = []

        """
        INNER FUNCTION TO RETIREVE A LIST OF ENTERTAINER OBJECTS
        @:param
        -   list of entertainer IDs
        """
        def retrieve_entertainer_list(entertainer_id_list):
            entertainer_list = []
            x = 0
            while x < len(entertainer_id_list):
                entertainer = Entertainer.objects.get(pk=entertainer_id_list[x])
                entertainer_list.append(entertainer)
                x += 1
            return entertainer_list


        ##################################################################################
        #   Loop used to extract the IDs of entertainers (AS INTEGERS) booked by user
        ##################################################################################
        for i in booked_entertainers_list:
            try:
                entertainer_id_list.append(int(i))
            except ValueError:
                pass    #   skip

        #############################################
        #   From the integer list of entertainer IDs
        #   RETRIEVE a list of entertainers
        #   using an inner function
        #############################################
        booked_entertainers = retrieve_entertainer_list(entertainer_id_list)
        #booked_entertainers = []
        log.debug('TESTING THE DEBUGGER')
        ##########################################################################################
        #   UNUSED:
        #   -   date_list: CONTAINS STRINGS OF DATES
        #   -   entertainer_id_list: CONTAINS STRING OF BOOKED ENTERTAINER IDS
        ##########################################################################################
        args = {'account_type_entertainer':account_type_entertainer,'bookings_made':bookings_made,'associated_entertainer':associated_entertainer,'booked_entertainers':booked_entertainers,'message':message}

        return render(request, 'accounts/profile.html',args)