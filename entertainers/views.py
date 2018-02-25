# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Entertainer
from django.contrib.auth.decorators import login_required
from .forms import EntertainerRegistrationForm
from django.contrib import messages
from accounts.models import User
from django.http import HttpResponse

####################
#   API Stuff
####################
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from entertainers.serializers import EntertainerSerializer
from entertainers.models import Entertainer
from django.db.models import Q
from django.core.paginator import Paginator

##########################################
#   LOGGING
##########################################
import logging
log = logging.getLogger(__name__)

####################
#   File Storage
####################
from django.core.files.storage import FileSystemStorage
from django.conf import settings

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
        logged_in = True

    ######################################################################
    #   WORKAROUND FOR PAYPAL NOT RETURNING POST OR GET TO paypal_return
    #   -   WILL USE A SESSION VATIABLE TO RECORD THE ENTERTAINER THAT
    #   -   WAS BOOKED
    ######################################################################

    request.session['entertainer_id'] = entertainer_id
    #   retrieve and save the current user session
    #current_user = request.user
    #request.session['booking_user_id'] = current_user.id

    ######################################################################
    #   END WORKAROUND
    ######################################################################

    entertainer = get_object_or_404(Entertainer, pk=entertainer_id)
    args = {'entertainer': entertainer,'get':get, 'logged_in':logged_in}
    return render(request,'entertainers/entertainer_profile.html',args)


@login_required()
def create_profile(request):
    edit = False
    profile_image = None
    image1 = None

    #if request.method == 'POST' and request.FILES['profile_image'] and request.FILES['image1']:
    if request.method == 'POST':

        #   If the form was submitted the contents of the form are passed in
        #   ALONG WITH THE LIST OF IMAGE URLS
        form = EntertainerRegistrationForm(request.user, request.POST, request.FILES)

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
    return render(request, 'entertainers/create_profile.html',{'form': form,'edit':edit})


@login_required()
def edit_profile(request,pk):
    edit = True
    entertainer = None
    if request.method == 'POST':
        entertainer = Entertainer.objects.get(pk=pk)
        #   If the form was submitted the contents of the form are passed in with the entertainer instance
        form = EntertainerRegistrationForm(request.user,request.POST,request.FILES,instance=entertainer)
        #   save the form if it is valid
        if form.is_valid():
            # save the currently logged in user as related to the Enterttainer profile
            # form.user = User
            form.save()
            messages.success(request, "You have successfully registered as an Entertainer")
            return redirect(reverse('entertainers:listings'))
        else:
            messages.error(request, "There was an issue and the Profile did not save")
    else:
        entertainer=Entertainer.objects.get(pk=pk)
        form = EntertainerRegistrationForm(request.user, instance=entertainer)

    return render(request, 'entertainers/edit_profile.html', {'pk':pk, 'edit':edit, 'title':entertainer.title, 'form':form})


@login_required()
def edit_profile_old(request,pk):
    edit = True
    if request.method == 'POST':
        """
        if request.POST['id']:
            pk = request.POST['id']
        #   retrieve the entertaineredit = True
        entertainer = Entertainer.objects.get(pk=pk)
        #   If page was just loaded then an empty form is displayed
        form = EntertainerRegistrationForm(request.user,request.POST,instance=entertainer)
        """
        #form = EntertainerRegistrationForm(request.session['_auth_user_id'],request.POST, instance=entertainer)
        #form = EntertainerRegistrationForm(request.user,request.POST)
        #form.save()
    else:
        """
        #entertainer = Entertainer.objects.get(pk=pk)
        #form = EntertainerRegistrationForm(request.user,instance=entertainer)
        """
        form = EntertainerRegistrationForm(request.user)
        #return redirect(reverse('entertainers:listings'))
    return render(request, 'entertainers/create_profile.html',{'form': form,'edit':edit})


#   increment the number of likes for an entertainer
def like(request,pk):
    """
        WILL NEED TO RETRIEVE THE USER ID TO SAVE THE ENTERTAINER AS LIKED BAND
        MAYBE TRANSFER THIS TO A FAVOURITE
    """
    #   USING POST INSTEAD OF GET AS SOME BROWSERS WILL SUBMIT THE REQUEST JUST BY TYPING INTO THE URL WITH NO PRESS OF ENTER
    if request.method == 'POST':
        #   retrieve the relevant entertainer
        entertainer = Entertainer.objects.get(pk=pk)
        #   increment the number of likes
        entertainer.likes_total += 1
        #   save the entertainer record
        entertainer.save()
        #   redirect back to the same page with the like_total incremented
        return redirect('entertainers:profile',pk)


#   increment the number of likes for an entertainer
def dislike(request,pk):
    #   USING POST INSTEAD OF GET AS SOME BROWSERS WILL SUBMIT THE REQUEST JUST BY TYPING INTO THE URL WITH NO PRESS OF ENTER
    if request.method == 'POST':
        #   retrieve the relevant entertainer
        entertainer = Entertainer.objects.get(pk=pk)
        #   increment the number of likes
        entertainer.dislikes_total += 1
        #   save the entertainer record
        entertainer.save()
        #   redirect back to the same page with the dislike_total incremented
        return redirect('entertainers:profile',pk)


#   class based view for handling request coming in for REST API
class EntertainerView(APIView):
    def get(self,request,pk=None):
        """
        -   (STEP 1) Query the ORM for a list of entertainers items from the Entertainer model
        -   (STEP 2) Serialize them to JSON and retrieve from .data property
        -   (STEP 3) Return the serialized data
        :param request:
        :return: serialized entertainers items
        """
        if pk is None:
            #   'self' is necessary when using a classed based view
            description = 'all'
            location = 'all'
            page = 'all'
            recordsPerPage = 8

            if self.request.GET['description'] is not None:
                if self.request.GET['description'] != 'all':
                    description = self.request.GET['description']

            if self.request.GET['location'] is not None:
                if self.request.GET['location'] != 'all':
                    location = self.request.GET['location']

            if self.request.GET['page'] is not None:
                if self.request.GET['page'] != 'all':
                    page = self.request.GET['page']


            #   (STEP 1A)
            #   -   Need to retrieve the total number of records
            #   -   Calculate and return the number of Pages
            #   -   Return the number of records per page
            #   -   Calculate the last page count
            #   -   Add these values to the serialized data as JSON and return


            #   (STEP 1B)
            if description != 'all' and location == 'all':
                entertainers = Entertainer.objects.filter(Q(description=description))
            elif description == 'all' and location != 'all':
                entertainers = Entertainer.objects.filter(Q(location=location))
            elif description != 'all' and location != 'all':
                entertainers = Entertainer.objects.filter(Q(description=description),Q(location=location))
            elif description == 'all' and location == 'all':
                entertainers = Entertainer.objects.all()
            else:
                entertainers = Entertainer.objects.all()

            #   (STEP 1C) - ONLY RETURN DATA RELEVANT TO THE SELECTED PAGE
            if page != 'all':
                paginator = Paginator(entertainers, recordsPerPage)
                num_pages = paginator.num_pages
                count = paginator.count
                entertainers = paginator.page(int(page))
                #   (STEP 2) - CONVERT DATA TO JSON
                #serializer = EntertainerSerializer(entertainers, many=True, num_pages=num_pages, count=count)
                serializer = EntertainerSerializer(entertainers, many=True, num_pages=num_pages, count=count)
            else:
                #   (STEP 2) - CONVERT DATA TO JSON
                serializer = EntertainerSerializer(entertainers,many=True)

            serialized_data = serializer.data
        else:
            #   (STEP 1)
            entertainers = Entertainer.objects.get(id=pk)
            #   (STEP 2)
            serializer = EntertainerSerializer(entertainers)
            serialized_data = serializer.data

        #   (STEP 3)
        return Response(serialized_data)

        """
        return Response({
            'count': paginator.count,
            'num_pages': paginator.num_pages,
            'results': serialized_data
        })
        """


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


    def delete(self,request,pk):
        """
        Handles DELETE request for 'Entertainer' endpoint
        -   (STEP 1) Retrieves an entertainer instance based on the primary key contained in the URL
        -   (STEP 2) Deletes the relevant instance
        -   (STEP 3) Returns a 204 (no content) status to indicate item was deleted
        :param request:
        :param pk:
        :return: status 204
        """
        #   (STEP 1)
        entertainer = Entertainer.objects.get(id=pk)
        #   (STEP 2)
        entertainer.delete()
        #   (STEP 3)
        return Response(status=status.HTTP_204_NO_CONTENT)

