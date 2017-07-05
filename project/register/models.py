# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    date=models.DateTimeField('DOB')


    def __str__(self):
        return self.fname
