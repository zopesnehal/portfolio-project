# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-09-03 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='imagefun',
        ),
    ]
