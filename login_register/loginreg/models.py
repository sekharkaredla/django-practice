# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Credentials(models.Model):
    rollno=models.CharField(primary_key=True,max_length=10)
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    sex=models.CharField(max_length=6,default='Male')
    marks=models.FloatField()

    def __str__(self):
        return self.rollno

    class Meta:
        unique_together=(('rollno','name','marks'))
