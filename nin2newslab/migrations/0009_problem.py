# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nin2newslab', '0008_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=10)),
                ('idx', models.IntegerField()),
                ('problem_str', models.TextField(default='')),
                ('explain_str', models.TextField(default='')),
                ('choice_list', models.TextField(default='')),
            ],
        ),
    ]
