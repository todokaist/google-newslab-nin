# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-28 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nin2newslab', '0033_nin2result'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Logic',
        ),
    ]