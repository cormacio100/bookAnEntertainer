# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.shortcuts import render,  redirect
from django.http import HttpResponse
from accounts.models import User
from entertainers.models import Entertainer

from django.contrib.auth.decorators import login_required


@csrf_exempt
@login_required()
def paypal_return(request):

    ###################################################################################################
    #   WORKAROUND FOR PAYPAL RETURNING AN EMPTY QUERYDICT {} FOR POST AND GET TO paypal_return VIEW
    #   -   WILL USE A SESSION VARIABLE TO RECORD THE ENTERTAINER THAT
    #   -   WAS BOOKED
    #   -   VARIABLE IS DELETED AFTER USE
    ###################################################################################################

    message = 'NO MESSAGE'
    entertainer_id = 0
    booking_user_id = 0
    auth_user_id = 0

    #   If the booking was made
    if 'entertainer_id' in request.session and '_auth_user_id' in request.session:
        #   retrieve the ID of the entertainer that was just booked
        #   and remove it from request.session
        entertainer_id = request.session['entertainer_id']
        del request.session['entertainer_id']

        #   retrieve the id of the logged in user who just made the booking
        booking_user_id = request.session['_auth_user_id']

        #*************************************************************************************************
        #   RETRIEVE THE USER OBJECT AND SAVE THE ENTERTAINER AS A BOOKED ENTERTAINER TO THE USER OBJECT
        #   -   save the entertainer_id to the String saved in user.booked_entertainer
        #   -   save the user
        # ************************************************************************************************
        user = User.objects.get(pk=booking_user_id)

        '''
            NEED TO SIMPLIFY THIS JUST TO CREATE A STRING AS FOLLOWS:
            booked_entertainer_str = str(entertainer_id)

            THEN IN THE ACCOUNTS MODULE ONLY NEED TO SPLIT THE STRING INTO INTEGERS
        '''

        #   booked_entertainer_str = "{'entertainer':'"+str(entertainer_id)+"','date':'2008-11-22'}"
        booked_entertainer_str = str(entertainer_id)

        if user.booked_entertainers == 'No Bookings':
            user.booked_entertainers = booked_entertainer_str+','
        else:
            user.booked_entertainers += booked_entertainer_str+','

        user.save()

        # *************************************************************************************************
        #   RETRIEVE THE Entertainer OBJECT AND DISPLAY A MESSAGE
        # *************************************************************************************************

        entertainer = Entertainer.objects.get(pk=entertainer_id)
        title = entertainer.title

        messages.success(request, "You have successfully booked "+title)
        return redirect(reverse('accounts:profile'))

        #message = 'entertainer ID and booking_user_id retrieved from session'
    else:
        message = 'Booking Failed'

    ######################################################################
    #   END WORKAROUND
    ######################################################################

    args = {'post':request.POST,'get':request.GET,'entertainer_id': entertainer_id,'booking_user_id':booking_user_id,'message':message}
    return render(request,'paypal_store/paypal_return.html',args)


@login_required()
def paypal_cancel(request):
    messages.error(request, "Booking Request Cancelled")
    return redirect(reverse('entertainers:listings'))