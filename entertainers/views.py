# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Entertainer
from django.contrib.auth.decorators import login_required
from .forms import EntertainerRegistrationForm
from django.contrib import messages
from accounts.models import User

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
        form = EntertainerRegistrationForm(request.POST)
        #   save the form if it is valid
        if form.is_valid():
            # save the currently logged in user as related to the Entertainer profile
            form.user = request.user
            form.save()
            messages.success(request, "You have successfully registered")
        else:
            messages.error(request, "There was an issue and the Profile did not save")
    else:
        #   If page was just loaded then an empty form is displayed
        form = EntertainerRegistrationForm()
    return render(request, 'entertainers/create_profile.html',{'form': form})



