# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 00:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nin2newslab', '0016_tablemodals'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TableModals',
            new_name='TableModal',
        ),
    ]