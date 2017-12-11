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
from rest_framework import status
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
    def get(self,request,description=None):
        """
        -   (STEP 1) Retrieve a full list OR a filtered list of entertainers items from the Entertainer model
        -   (STEP 2) Serialize them to JSON and retrieve from .data property
        -   (STEP 3) Return the serialized data
        :param request:
        :return: serialized entertainers items
        """
        if description is None:
            #   (STEP 1) - ALL
            entertainers = Entertainer.objects.all()
            #   (STEP 2)
            serializer = EntertainerSerializer(entertainers,many=True)
            serialized_data = serializer.data

        else:
            #   (STEP 1) - FILTERED
            entertainers = Entertainer.objects.get(description=description)
            #   (STEP 2)
            serializer = EntertainerSerializer(entertainers)
            serialized_data = serializer.data

        #   (STEP 3)
        return Response(serialized_data)

    def post(self,request):
        """
        This view will:
        -   (STEP 1) take the .data property from 'request' obj and deserialize it into an ENTERTAINER object
        -   (STEP 2) Check to see if valid
            -   If YES then save in the DB and return 201 Response
            -   If NO then display an error and return a 400 Response
        :param request:
        :return:
        """
        #   (STEP 1)
        serializer = EntertainerSerializer(data=request.data)
        #   (STEP 2)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    def put(self,request,pk):
        """
        UPDATES AN ENTERTAINER:

        -   (STEP 1) Retrieves an Entertainer instance based on primary key in the URL
        -   (STEP 2) Takes the data property from the 'Request' object and updates the relevant Entertainer instance
        -   (STEP 3) Checks if valid and whether it can be deserialialized
        -   (STER 4) Returns the updated object if the update was successful
            -   if not, then returns 400(bad request)
        :param request:
        :return: updated object or rsponse 404
        """
        #   (STEP 1)
        entertainer = Entertainer.objects.get(id=pk)
        #   (STEP 2)
        serializer = EntertainerSerializer(entertainer,data=request.data)
        #   (STEP 3)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data)
