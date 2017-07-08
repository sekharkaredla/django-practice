# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-08 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=40)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('res_num', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('res_name', models.CharField(max_length=100, unique=True)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='resources',
            unique_together=set([('res_num', 'res_name', 'capacity')]),
        ),
        migrations.AddField(
            model_name='request',
            name='res_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcealloc.Resources'),
        ),
        migrations.AddField(
            model_name='request',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcealloc.Credentials'),
        ),
        migrations.AlterUniqueTogether(
            name='credentials',
            unique_together=set([('username', 'is_admin', 'password')]),
        ),
        migrations.AlterUniqueTogether(
            name='request',
            unique_together=set([('username', 'res_num', 'request_date')]),
        ),
    ]
