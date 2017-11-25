# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == 'GET':
        args = {'choose_account_type': True}
    else:
        args = {'choose_account_type': False}

    return render(request, 'accounts/register.html', args)