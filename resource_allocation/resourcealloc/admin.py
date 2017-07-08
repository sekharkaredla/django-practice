# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from resourcealloc.models import Credentials, Resources, Request
# Register your models here.

class CredentialAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'password'
    )
    list_filter = (
        'username',
        'password'
    )

class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        'res_num',
        'res_name'
    )

class RequestAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'resource',
        'request_date'
    )

admin.site.register(Credentials,CredentialAdmin)
admin.site.register(Resources,ResourceAdmin)
admin.site.register(Request,RequestAdmin)
