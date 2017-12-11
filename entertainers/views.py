# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Entertainer
from django.contrib.auth.decorators import login_required
from .forms import EntertainerRegistrationForm
from django.contrib import messages
from accounts.models import User

################
#   API Stuff
################
from rest_framework.response import Response
from rest_framework.views import APIView
from entertainers.serializers import EntertainerSerializer
from entertainers.models import Entertainer


# Create your views here.
def listings(request):
    entertainers = Entertainer.objects.all()
    args = {'entertainers': entertainers}
    return render(request, 'entertainers/listings.html',args)


#   display the detail of individual entertainers
def display_entertainer_profile(request,entertainer_id):
    get = False
    if request.method == 'GET':
        get = True
    logged_in = False
    if request.user is not None:
        print('request.user is:')
        print(request.user)
        logged_in = True
    entertainer = get_object_or_404(Entertainer, pk=entertainer_id)
    args = {'entertainer': entertainer,'get':get, 'logged_in':logged_in}
    return render(request,'entertainers/entertainer_profile.html',args)


@login_required()
def create_profile(request):

    if request.method == 'POST':
        #   If the form was submitted the contents of the form are passed in
        form = EntertainerRegistrationForm(request.user,request.POST)
        #   save the form if it is valid
        if form.is_valid():
            # save the currently logged in user as related to the Enterttainer profile
            #form.user = User
            form.save()
            messages.success(request, "You have successfully registered as an Entertainer")
            return redirect(reverse('entertainers:listings'))
        else:
            messages.error(request, "There was an issue and the Profile did not save")
    else:
        #   If page was just loaded then an empty form is displayed
        form = EntertainerRegistrationForm(request.user)
    return render(request, 'entertainers/create_profile.html',{'form': form})

#   class based view for handling request coming in for REST API
class EntertainerView(APIView):
    def get(self,request):
        """
        -   (STEP 1) Retrieve a full list of entertainers items from the Entertainer model
        -   (STEP 2) Serialize them to JSON and retrieve from .data property
        -   (STEP 3) Return the serialized data
        :param request:
        :return: serialized entertainers items
        """
        #   (STEP 1)
        entertainers = Entertainer.objects.all()
        #   (STEP 2)
        serializer = EntertainerSerializer(entertainers,many=True)
        serialized_data = serializer.data
        #   (STEP 3)
        return Response(serialized_data)
