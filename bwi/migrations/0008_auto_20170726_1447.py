# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwi', '0007_auto_20170724_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='division',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='divisions',
            field=models.ManyToManyField(blank=True, null=True, to='bwi.Division'),
        ),
    ]
