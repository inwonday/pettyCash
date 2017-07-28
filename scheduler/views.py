# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import urllib2

# Create your views here.

#View Format
#<Three chat client code>_<Three digit client number>_<Three digit URL number>
#Comment on top

def abc_def_001():
    pass

#Status
def sch_001_001():
    #Send mail for business
    pass

#Delivery note sheet sync
def cac_002_001():
    #url: delivery.carcrew.in/Delivery/api/sync_sheet
    urllib2.urlopen("http://delivery.carcrew.in/Delivery/api/sync_sheet").read()

#Delivery note daily status
def cac_002_002():
    urllib2.urlopen("http://delivery.carcrew.in/Delivery/schedule_date_cronjob").read()

#Delivery daily status
def cac_002_003():
    urllib2.urlopen("http://delivery.carcrew.in/Delivery/schedule_date_cronjob").read()


