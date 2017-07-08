# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Credentials(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=40, blank=False)
    is_admin = models.BooleanField(blank=False, default=False)

    class Meta:
        unique_together = (('username', 'is_admin', 'password'))

    def __str__(self):
        return self.username


class Resources(models.Model):
    res_num = models.CharField(max_length=10, primary_key=True)
    res_name = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField()

    class Meta:
        unique_together = (('res_num', 'res_name', 'capacity'))

    def __str__(self):
        return self.res_name


class Request(models.Model):
    username = models.ForeignKey(to=Credentials)
    resource = models.ForeignKey(to=Resources)
    request_date = models.DateField(blank=False)

    class Meta:
        unique_together = (('username', 'resource', 'request_date'))

    def __str__(self):
        return str(self.request_date)
