# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 23:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Password',
            new_name='password',
        ),
    ]
