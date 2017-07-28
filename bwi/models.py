# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bankName = models.CharField(max_length=60, null=True, blank=True)
    bankAccountNumber = models.CharField(max_length=30, null=True, blank=True)
    ifscCode = models.CharField(max_length=30, null=True, blank=True)
    remarks = models.CharField(max_length=30, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % self.name

class Division(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=30, null=True, blank=True)
    head = models.CharField(max_length=30, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bankName = models.CharField(max_length=60, null=True, blank=True)
    bankAccountNumber = models.CharField(max_length=30, null=True, blank=True)
    ifscCode = models.CharField(max_length=30, null=True, blank=True)
    remarks = models.CharField(max_length=30, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % self.name

# Create your models here.
TITLE_CHOICES = (
    ('Mr.', _("Mr.")),
    ('Mrs.', _("Mrs.")),
    ('Ms.', _("Ms."))
)
class UserProfile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(choices=TITLE_CHOICES, max_length=5, default="Mr.")
    company = models.ForeignKey(Company, null=True, blank=True)
    divisions = models.ManyToManyField(Division)
    Phone_No = models.CharField(max_length=11, null=True, blank=True)
    UserType = models.CharField(max_length=15, null=True, blank=True)
    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)
    Deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' %self.user.username

class PettyCashEntry(models.Model):
    division = models.ForeignKey(Division, null=True, blank=True)
    company = models.ForeignKey(Company, null=True, blank=True)
    profile = models.ForeignKey(UserProfile, null=True, blank=True)
    receiptNumber =  models.CharField(max_length=10, null=True, blank=True)
    paymentType =  models.CharField(max_length=10, null=True, blank=True)
    beneficiary = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    uom = models.CharField(max_length=5, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    unitPrice = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    totalAmount = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    category = models.CharField(max_length=40, null=True, blank=True)
    remarks =  models.CharField(max_length=30, null=True, blank=True)
    createdAt =  models.DateTimeField(auto_now_add=True)

class PettyCashReceipt(models.Model):
    division = models.ForeignKey(Division, null=True, blank=True)
    company = models.ForeignKey(Company, null=True, blank=True)
    profile = models.ForeignKey(UserProfile, null=True, blank=True)
    receiptNumber =  models.CharField(max_length=10, null=True, blank=True)
    referenceNumber =  models.CharField(max_length=10, null=True, blank=True)
    paymentType =  models.CharField(max_length=10, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    amountReceived = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    remarks =  models.CharField(max_length=30, null=True, blank=True)
    createdAt =  models.DateTimeField(auto_now_add=True)
    entryNumber = models.IntegerField(blank=True, null=True)

class OperationalTransaction(models.Model):
    profile = models.ForeignKey(UserProfile, null=True, blank=True)
    company = models.ForeignKey(Company, null=True, blank=True)
    division = models.ForeignKey(Division, null=True, blank=True)
    opFrom = models.DateTimeField(blank=True,null=True)
    opTo = models.DateTimeField(blank=True,null=True)
    remarks =  models.CharField(max_length=100, null=True, blank=True)
    customerName =  models.CharField(max_length=30, null=True, blank=True)
    createdAt =  models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Transaction(models.Model):
    name =  models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.name)

class Category(models.Model):
    name =  models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.name)

class TaskCategory(models.Model):
    name =  models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.name)
