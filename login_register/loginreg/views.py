# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import Credentials

from django.http import HttpResponse,HttpResponseForbidden
# Create your views here.

def login(request):
    return render(request, 'loginreg/login.html')


def send_data(request):
    credential=Credentials.objects.get(rollno=request.POST['roll'])
    context={
        "name":credential.name,
        "sex": credential.sex,
        "marks": credential.marks
    }
    if credential.password == request.POST['pass']:
        return render(request,'loginreg/login_done.html',context)
    else:
        return HttpResponseForbidden('password wrong')