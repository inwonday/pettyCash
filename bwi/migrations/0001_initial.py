# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 07:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('bankName', models.CharField(blank=True, max_length=60, null=True)),
                ('bankAccountNumber', models.CharField(blank=True, max_length=30, null=True)),
                ('ifscCode', models.CharField(blank=True, max_length=30, null=True)),
                ('remarks', models.CharField(blank=True, max_length=30, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('head', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('bankName', models.CharField(blank=True, max_length=60, null=True)),
                ('bankAccountNumber', models.CharField(blank=True, max_length=30, null=True)),
                ('ifscCode', models.CharField(blank=True, max_length=30, null=True)),
                ('remarks', models.CharField(blank=True, max_length=30, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bwi.Company')),
            ],
        ),
        migrations.CreateModel(
            name='PettyCashEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiptNo', models.CharField(blank=True, max_length=10, null=True)),
                ('paymentType', models.CharField(blank=True, max_length=10, null=True)),
                ('beneficiary', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('uom', models.CharField(blank=True, max_length=5, null=True)),
                ('unitPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('totalAmount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('category', models.CharField(blank=True, max_length=40, null=True)),
                ('remarks', models.CharField(blank=True, max_length=30, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('entryNumber', models.IntegerField()),
                ('divisionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bwi.Division')),
            ],
        ),
        migrations.CreateModel(
            name='PettyCashReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiptNumber', models.CharField(blank=True, max_length=10, null=True)),
                ('referenceNumber', models.CharField(blank=True, max_length=10, null=True)),
                ('paymentType', models.CharField(blank=True, max_length=10, null=True)),
                ('beneficiary', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('amountReceived', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('remarks', models.CharField(blank=True, max_length=30, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('entryNumber', models.IntegerField()),
                ('divisionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bwi.Division')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_No', models.CharField(blank=True, max_length=11, null=True)),
                ('UserType', models.CharField(max_length=15)),
                ('Created_At', models.DateTimeField(auto_now_add=True)),
                ('Updated_At', models.DateTimeField(auto_now=True)),
                ('Deleted', models.BooleanField(default=False)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]