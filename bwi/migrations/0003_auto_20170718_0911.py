# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwi', '0002_auto_20170718_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pettycashentry',
            name='entryNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='UserType',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
