# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *


# Register your models here.

class CredentialAdmin(admin.ModelAdmin):
    pass


class ResourceAdmin(admin.ModelAdmin):
    pass


class RequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Credential, CredentialAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Request, RequestAdmin)
