# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bwi', '0006_auto_20170722_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='pettycashentry',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bwi.Company'),
        ),
        migrations.AddField(
            model_name='pettycashreceipt',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bwi.Company'),
        ),
    ]
