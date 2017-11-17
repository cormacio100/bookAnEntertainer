# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Entertainer

# Create your views here.
def list_entertainers_all(request):
    entertainers = Entertainer.objects.all()
    args = {'entertainers': entertainers}
    return render(request, 'entertainers/entertainers.html',args)


#   display the detail of individual entertainers
def display_entertainer_profile(request,entertainer_id):
    args = {'entertainer_id': entertainer_id}
    return render(request,'entertainers/entertainer_profile.html',args)


