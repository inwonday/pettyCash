# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    pass
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location','bankName')
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','bankName','company_id')
class PettyCashEntryAdmin(admin.ModelAdmin):
     list_display = ('id', 'receiptNumber','paymentType','totalAmount')
class PettyCashReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'receiptNumber','paymentType','amountReceived')
class OperationalTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'remarks','opFrom','opTo')
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(PettyCashEntry, PettyCashEntryAdmin)
admin.site.register(PettyCashReceipt, PettyCashReceiptAdmin)
admin.site.register(OperationalTransaction, OperationalTransactionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)
