# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-06 16:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mini_insta', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([('image', 'owner')]),
        ),
    ]
