# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bwi', '0010_auto_20170727_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operationaltransaction',
            old_name='cutomerName',
            new_name='customerName',
        ),
    ]
