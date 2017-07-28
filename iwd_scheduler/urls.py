"""iwd_scheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bwi import views as bwiViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^addPettyCashEntry', bwiViews.addPettyCashEntry, name="addPettyCashEntry"),
    url(r'^addPettyCashReceipt', bwiViews.addPettyCashReceipt, name="addPettyCashReceipt"),
    url(r'^pettyCashEntries', bwiViews.pettyCashEntries),
    url(r'^pettyCashReceipts', bwiViews.pettyCashReceipts),
    url(r'^pettycash', bwiViews.home, name="adminHome"),
    url(r'^operational', bwiViews.operational),
    url(r'^addActivity', bwiViews.addActivity, name="addActivity"),
    url(r'^activities', bwiViews.operationalTransactions),
    url(r'^login', bwiViews.loginuser, name="login"),
    url(r'^logout', bwiViews.logoutuser),
    url(r'^rough', bwiViews.rough),
]