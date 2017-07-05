# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from models import Person


# Create your views here.
def input(request):
    return render(request, 'register/register.html')


def output(request):
    Person.objects.create(
        fname=request.POST['fname'],
        lname=request.POST['lname'],
        date=request.POST['dob']
    )
    return HttpResponse('success')


def show(request):
    all_persons = Person.objects.all()
    data_objects = []
    for each_person in all_persons:
        person_dict = {
            'fname': each_person.fname,
            'lname': each_person.lname,
            'dob': each_person.date
        }
        data_objects.append(person_dict)

    return render(request, 'register/show_data.html',{"data":data_objects})
