# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def list_entertainers_all(request):
    return render(request, 'entertainers/entertainers.html')
