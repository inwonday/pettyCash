# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 15:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bwi', '0009_auto_20170727_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pettycashreceipt',
            name='beneficiary',
        ),
        migrations.AddField(
            model_name='operationaltransaction',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bwi.Company'),
        ),
    ]
