# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request=None):
    print request.user.is_anonymous()
    if request.user.is_anonymous():
        return redirect('login')
    else:
        profile = UserProfile.objects.filter(user=request.user.pk).first()
        if profile.UserType == 'admin':
            companies = Company.objects.all()
            divisions = Division.objects.all()
            transactions = Transaction.objects.all()
            return render(request, 'bwi/adminHome.html', {'companies': companies,'divisions':divisions,'transactions':transactions})
        else:
            transactions = Transaction.objects.all()
            return render(request, 'bwi/employeeHome.html', {'transactions':transactions, 'profile': profile, 'divisions': profile.divisions.all()})

def employeeHome(request=None):
    companies = Company.objects.all()
    divisions = Division.objects.all()
    transactions = Transaction.objects.all()
    print companies
    return render(request, 'bwi/adminHome.html', {'companies': companies,'divisions':divisions,'transactions':transactions})


def operational(request=None):
    return render(request, 'bwi/operational.html')

def pettyCashEntries(request=None):
    if request.user.is_anonymous():
        return redirect('login')
    user_profile = UserProfile.objects.filter(user=request.user.pk).first()
    if user_profile and user_profile.UserType != 'admin':
        entries = PettyCashEntry.objects.filter(profile=user_profile);
    else:
        entries = PettyCashEntry.objects.all()
    print  PettyCashReceipt.objects.aggregate(Sum('amountReceived'))
    print PettyCashEntry.objects.aggregate(Sum('totalAmount'))
    bal = PettyCashReceipt.objects.aggregate(Sum('amountReceived')).get('amountReceived__sum') - PettyCashEntry.objects.aggregate(Sum('totalAmount')).get('totalAmount__sum')

    return render(request, 'bwi/pettyCashEntries.html',{'entries': entries, 'balance':bal, 'profile': user_profile})

def pettyCashReceipts(request=None):
    if request.user.is_anonymous():
        return redirect('login')
    user_profile = UserProfile.objects.filter(user=request.user.pk).first()
    if user_profile and user_profile.UserType != 'admin':
        receipts = PettyCashReceipt.objects.filter(profile=user_profile)
    else:
        receipts = PettyCashReceipt.objects.all()

    bal = PettyCashReceipt.objects.aggregate(Sum('amountReceived')).get('amountReceived__sum') - PettyCashEntry.objects.aggregate(Sum('totalAmount')).get('totalAmount__sum')
    return render(request, 'bwi/pettyCashReceipts.html',{'receipts': receipts, 'balance':bal, 'profile': user_profile})

def addPettyCashEntry(request=None):
    if request.user.is_anonymous():
        return redirect('login')
    categories = Category.objects.all()
    if request.method == 'POST':
        print request.POST
        data = request.POST
        dataDict = data.dict()
        dataDict.pop('csrfmiddlewaretoken', None)
        print request.user
        user_profile = UserProfile.objects.filter(user=request.user.pk).first()
        if user_profile:
            dataDict["profile"] = user_profile
            dataDict["company"] = user_profile.company
            if user_profile.divisions.all():
                dataDict["division"] = user_profile.divisions.all()[0]
        pce = PettyCashEntry.objects.create(**dataDict)
        return redirect('addPettyCashEntry')
    else:
        user_profile = UserProfile.objects.filter(user=request.user.pk).first()
        return render(request, 'bwi/addPettyCashEntry.html', {'categories':categories, 'profile': user_profile})

def addPettyCashReceipt(request=None):
    if request.user.is_anonymous():
        return redirect('login')
    if request.method == 'POST':
        print request.POST
        data = request.POST
        dataDict = data.dict()
        dataDict.pop('csrfmiddlewaretoken', None)
        user_profile = UserProfile.objects.filter(user=request.user.pk).first()
        if user_profile:
            dataDict["profile"] = user_profile
            dataDict["company"] = user_profile.company
            if user_profile.divisions.all():
                dataDict["division"] = user_profile.divisions.all()[0]
        pce = PettyCashReceipt.objects.create(**dataDict)
        return redirect('addPettyCashReceipt')
    else:
        user_profile = UserProfile.objects.filter(user=request.user.pk).first()
        return render(request, 'bwi/addPettyCashReceipt.html', {'profile': user_profile})

def getPettyCashEntry(request=None):
    pass
def getPettyCashReceipt(request=None):
    pass

def addActivity(request=None):
    if request.user.is_anonymous():
        return redirect('login')
    if request.method == 'POST':
        print request.POST
        data = request.POST
        dataDict = data.dict()
        date = dataDict.get("date")
        fromTime = dataDict.get("opFrom")
        toTime = dataDict.get("opTo")
        print dataDict
        opFrom = datetime.strptime(date + ':' + fromTime, "%Y-%m-%d:%H:%M")
        opTo = datetime.strptime(date + ':' + toTime, "%Y-%m-%d:%H:%M")
        ot = OperationalTransaction()
        ot.customerName = dataDict.get("customerName")
        print ot.customerName
        dataDict.pop('csrfmiddlewaretoken', None)
        user_profile = UserProfile.objects.filter(user=request.user.pk).first()
        if user_profile:
            ot.profile = user_profile
            ot.company = user_profile.company
            if user_profile.divisions.all():
                ot.division = user_profile.divisions.all()[0]

        ot.opFrom = opFrom
        ot.opTo = opTo
        ot.remarks = dataDict.get("remarks")
        ot.save()

        return redirect('addActivity')
    else:
        user_profile = UserProfile.objects.filter(user=request.user.pk).first()
        return render(request, 'bwi/addActivity.html', {'profile': user_profile})

def operationalTransactions(request=None):
    if request.user.is_anonymous():
        return redirect('login')
    user_profile = UserProfile.objects.filter(user=request.user.pk).first()
    if user_profile and user_profile.UserType != 'admin':
        activities = OperationalTransaction.objects.filter(profile=user_profile)
    else:
         activities = OperationalTransaction.objects.all()
    return render(request, 'bwi/activities.html',{'activities':activities, 'profile':user_profile})

def loginuser(request):
    if request.method == 'POST':
        data = request.POST.dict()
        username = data.get('username', None)
        password = data.get('password', None)
        print username + ' ' + password
        user = authenticate(username=username, password=password)
        if not user :
            return render(request, 'bwi/login.html')
        login(request, user)
        user_profile = UserProfile.objects.filter(user=user.pk).first()
        if user_profile.UserType == 'admin':
            return redirect('adminHome')
        else:
            return redirect('adminHome')
    else:
        companies = Company.objects.all()
        divisions = Division.objects.all()
        return render(request, 'bwi/login.html', {'companies':companies, 'divisions':divisions})


def logoutuser(request=None):
    logout(request)
    return redirect('login')

#DO NOT TOUCH THIS FUNCTION
def rough(request=None):
    if request.method == 'POST':
        data = request.POST.dict()
        print data
        username = data.get('username', None)
        passwordOld = data.get('passwordOld', None)
        passwordNew = data.get('passwordNew', None)
        passwordConfirm = data.get('passwordNewConfirm', None)
        if passwordNew == passwordConfirm:
            user = authenticate(username=username, password=passwordOld)
            if user is not None:
                print passwordNew
                user.set_password(passwordNew)
                user.save()
                print  authenticate(username=username, password=passwordOld)
                print 'all godod'
                return redirect('login')
        return render(request, 'bwi/rough.html')
    else:
        companies = Company.objects.all()
        divisions = Division.objects.all()
        return render(request, 'bwi/rough.html', {'companies':companies, 'divisions':divisions})
