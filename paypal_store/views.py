# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User

@csrf_exempt
def paypal_return(request):

    ###################################################################################################
    #   WORKAROUND FOR PAYPAL RETURNING AN EMPTY QUERYDICT {} FOR POST AND GET TO paypal_return VIEW
    #   -   WILL USE A SESSION VARIABLE TO RECORD THE ENTERTAINER THAT
    #   -   WAS BOOKED
    #   -   VARIABLE IS DELETED AFTER USE
    ###################################################################################################

    message = 'NO MESSAGE'
    entertainer_id = 0
    current_user = None

    if 'entertainer_id' in request.session:
        entertainer_id = request.session['entertainer_id']
        del request.session['entertainer_id']
        current_user = request.user
        user_id = current_user.id
        messages.success(request,'Entertainer Booked by user ID'+str(current_user.id))
        message = 'Entertainer Booked by user ID'+str(current_user.id)
    else:
        message = 'Entertainer was NOT Booked by user'

    '''
    if 'entertainer_id' not in request.session:
        message2 =  'entertainer_id has been removed:'
    else:
        message2 = 'entertainer_id still exists:'
    '''
    ######################################################################
    #   END WORKAROUND
    ######################################################################

    args = {'post':request.POST,'get':request.GET,'entertainer_id': entertainer_id,'message':message,'user_id':user_id}
    return render(request,'paypal_store/paypal_return.html',args)

def paypal_cancel(request):
    args = {'post':request.POST,'get': request.GET}
    return render(request,'paypal_store/paypal_cancel.html',args)