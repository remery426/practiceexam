# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 22:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20161213_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='username',
        ),
    ]