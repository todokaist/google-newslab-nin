# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-16 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nin2newslab', '0027_auto_20160215_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userchoice',
            old_name='json',
            new_name='chosen_json',
        ),
        migrations.AddField(
            model_name='userchoice',
            name='user_json',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]