# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
# Create your views here.
from models import Credential
from models import Request
from models import Resource


def get_requests_of_users():
    requests = Request.objects.all()
    context = []

    for each_request in requests:
        context_dict = {
            'user': each_request.user.username,
            'resource': each_request.resource.res_name,
            'time': each_request.date
        }
        context.append(context_dict)
    return context


def get_resources_for_user():
    resources = Resource.objects.all()
    context = []
    for each_resource in resources:
        context_dict = {
            'res_num': each_resource.res_num,
            'res_name': each_resource.res_name,
            'capacity': each_resource.res_capacity
        }
        context.append(context_dict)
    return context

class Index(View):
    def get(self, request):
        user = request.session.get('user', '')
        if user == '':
            return render(request, 'resourcealloc/index.html')
        else:
            context = get_resources_for_user()
            return render(request, 'resourcealloc/user.html', {'resources': context})



class LoginCheck(View):

    def post(self, request):
        user = request.POST.get('name')
        password = request.POST.get('pass')
        credentials = Credential.objects.filter(username=user)
        if len(credentials) == 0:
            return redirect('/resourcealloc')
        credentials = credentials[0]
        if user == credentials.username and password == credentials.password:
            request.session['user'] = user
            if credentials.is_admin:
                context = get_requests_of_users()
                return render(request, 'resourcealloc/admin.html', {'requests': context})
            else:
                context = get_resources_for_user()
                return render(request, 'resourcealloc/user.html', {'resources': context})
        else:
            return redirect('/resourcealloc')
    # def get(self,request):
    #     user=request.session.get('user','')
    #     if user == '':
    #         return redirect('/resourcealloc')
    #     else:
    #         context = self.get_resources_for_user()
    #         return render(request, 'resourcealloc/user.html', {'resources': context})


class Register(View):
    def get(self, request):
        return render(request, 'resourcealloc/register.html')


class RegisterCheck(View):
    def post(self, request):
        user = request.POST.get('user')
        password = request.POST.get('pass')
        credential = Credential.objects.filter(username=user)
        if len(credential) != 0:
            return redirect('/resourcealloc/register')
        Credential.objects.create(
            username=user,
            password=password,
            is_admin=False
        )
        return redirect('/resourcealloc')


class RandomRequest(View):
    def post(self, request):
        user = request.session.get('user', '')
        if user == '':
            return redirect('/resourcealloc')
        resource = Resource.objects.get(res_num=1)
        thirty_days = datetime.timedelta(days=30)
        credential=Credential.objects.get(username=user)
        Request.objects.create(
            user=credential,
            resource=resource,
            date=datetime.date.today() + thirty_days
        )
        return render(request, 'resourcealloc/success.html')
