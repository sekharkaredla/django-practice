# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Credential(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    is_admin = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.username


class Resource(models.Model):
    res_num = models.IntegerField(primary_key=True)
    res_name = models.CharField(max_length=50)
    res_capacity = models.IntegerField()

    def __str__(self):
        return self.res_name


class Request(models.Model):
    user = models.ForeignKey(Credential)
    resource = models.ForeignKey(Resource)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.user) + ' ' + str(self.resource)
