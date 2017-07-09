# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from models import Credentials, Request, Resources

from django.views import View


# Create your views here.

class Index(View):
    def get(self,request):
        return render(request, 'resourcealloc/index.html', context=None)


class Login_check(View):
    def post(self,request):
        username = request.POST.get('name')
        get_record = Credentials.objects.filter(username=username)
        if len(get_record) == 1:
            get_record = get_record[0]
            if get_record.password == request.POST.get('pass'):
                request.session['login'] = True
                if get_record.is_admin:
                    requests = Request.objects.all()
                    request_list = []
                    for each_request in requests:
                        request_dict = {
                            'username': each_request.username.username,
                            'res_num': each_request.resource.res_num,
                            'res_name': each_request.resource.res_name,
                            'capacity': each_request.resource.capacity,
                            'request_date': each_request.request_date
                        }
                        request_list.append(request_dict)
                    print request_list
                    return render(request, 'resourcealloc/admin.html', {'name': username, 'requests': request_list})
                else:
                    resources = Resources.objects.all()
                    resource_list = []
                    for each_resource in resources:
                        resource_dict = {
                            'res_num': each_resource.res_num,
                            'res_name': each_resource.res_name,
                            'capacity': each_resource.res_name
                        }
                        resource_list.append(resource_dict)
                    print resource_list
                    return render(request, 'resourcealloc/user.html', {'name': username, 'resources': resource_list})
            else:
                return redirect('/resourcealloc')
        else:
            return redirect('/resourcealloc')