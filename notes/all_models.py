from django.db import models

from django.contrib.auth.models import User

class AccountSection(models.Model):
    name = models.TextField()

class AccountGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    section_in_accounts = models.IntegerField()
    pandl = models.SmallIntegerField()
    sequence_in_tb = models.ForeignKey(AccountSection)
    parent_group = models.ForeignKey('self')

class Area(models.Model):
    code = models.CharField(max_length=3)
    description = models.CharField(max_length=25, blank=True)

class AssetManager(models.Model):
    stock_id = models.CharField(max_length=20, blank=True)
    serial_no = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=15, blank=True)
    cost = models.DecimalField(max_digits=12, decimal_places=4)
    depn = models.DecimalField(max_digits=12, decimal_places=4)
    date_purchased = models.DateField()
    disposal_value = models.IntegerField()

class AuditTrail(models.Model):
    transaction_date = models.DateTimeField()
    user_id = models.ForeignKey(User)
    query_string = models.TextField()

class BankAccount(models.Model):
    account_code = models.CharField(max_length=20, unique=True)
    curr_code = models.CharField(max_length=3)
    invoice = models.SmallIntegerField()
    bank_account_code = models.CharField(max_length=50, blank=True)
    bank_account_name = models.CharField(max_length=50, blank=True)
    bank_account_number = models.CharField(max_length=50, blank=True)
    bank_address = models.CharField(max_length=50, blank=True)

class SysType(models.Model):
    name = models.CharField(max_length=50)
    no = models.IntegerField()

class BankTransaction(models.Model):
    trans_type = models.ForeignKey(SysType)
    trans_no = models.BigIntegerField()
    bank_act = models.ForeignKey(BankAccount)
    ref = models.CharField(max_length=50)
    amount_cleared = models.DecimalField(max_digits=12, decimal_places=4)
    exchange_rate = models.DecimalField(max_digits=12, decimal_places=4)
    functional_exchange_rate = models.DecimalField(max_digits=12, decimal_places=4)
    trans_date = models.DateField()
    bank_trans_type = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=12, decimal_places=4)
    curr_code = models.CharField(max_length=3)

class StockCategory(models.Model):
    description = models.CharField(max_length=20)
    stock_type = models.CharField(max_length=1)
    stock_act = models.IntegerField()
    adj_gl_act = models.IntegerField()
    issue_gl_act = models.IntegerField()
    purch_price_var_act = models.IntegerField()
    material_usage_var_act = models.IntegerField()
    wip_act = models.IntegerField()

class TaxCategory(models.Model):
    name = models.CharField(max_length=30)

class UnitsOfMeasure(models.Model):
    name = models.CharField(max_length=15)

class StockMaster(models.Model):
    stock_id = models.CharField(max_length=20)
    category_id = models.ForeignKey(StockCategory)
    desc = models.CharField(max_length=50)
    long_desc = models.TextField()
    units = models.ForeignKey(UnitsOfMeasure)

class BOM(models.Model):
    pass