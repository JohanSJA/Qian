from django.db import models

from django.contrib.auth.models import User


class AccountSection(models.Model):
    name = models.TextField()
    
    def __unicode__(self):
        return self.name


class AccountGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    section_in_accounts = models.IntegerField()
    profit_and_loss = models.SmallIntegerField()
    sequence_in_tb = models.ForeignKey(AccountSection)
    parent_group = models.ForeignKey('self')
    
    def __unicode__(self):
        return self.name


class Area(models.Model):
    code = models.CharField(max_length=3)
    description = models.CharField(max_length=25, blank=True)


class AssetManager(models.Model):
    stock_id = models.CharField(max_length=20, blank=True)
    serial_no = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=15, blank=True)
    cost = models.DecimalField(max_digits=20, decimal_places=4)
    depn = models.DecimalField(max_digits=20, decimal_places=4)
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
    amount_cleared = models.DecimalField(max_digits=20, decimal_places=4)
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=4)
    functional_exchange_rate = models.DecimalField(max_digits=12, decimal_places=4)
    trans_date = models.DateField()
    bank_trans_type = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=20, decimal_places=4)
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


class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=15)


class StockMaster(models.Model):
    code = models.CharField(max_length=20)
    category = models.ForeignKey(StockCategory)
    short_description = models.CharField(max_length=50)
    long_description = models.TextField(blank=True)
    units = models.ForeignKey(UnitOfMeasure, verbose_name="unit of measure")
    mb_flag = models.CharField("Assembly, Kit, Manufactured or Service/Labour", max_length=1, choices = [
                ("A", "Assembly"),
                ("K", "Kit"),
                ("M", "Manufactured"),
                ("G", "Phantom"),
                ("B", "Purchased"),
                ("D", "Service/Labour")
            ])
    actual_cost = models.DecimalField(max_digits=20, decimal_places=4)
    last_cost = models.DecimalField(max_digits=20, decimal_places=4)
    material_cost = models.DecimalField(max_digits=20, decimal_places=4)
    labour_cost = models.DecimalField(max_digits=20, decimal_places=4)
    overhead_cost = models.DecimalField(max_digits=20, decimal_places=4)
    lowest_level = models.SmallIntegerField()
    discontinued = models.BooleanField()
    controlled = models.BooleanField()
    eoq = models.FloatField()
    volume = models.DecimalField(max_digits=20, decimal_places=4)
    kgs = models.DecimalField(max_digits=20, decimal_places=4)
    barcode = models.CharField(max_length=50)
    discount_category = models.CharField(max_length=2)
    tax_category = models.ForeignKey(TaxCategory)
    serialised = models.BooleanField()
    appendfile = models.CharField(max_length=40)
    perishable = models.BooleanField()
    decimal_places = models.SmallIntegerField()
    pan_size = models.FloatField()
    shrinkage_factor = models.FloatField()
    next_serial_no = models.BigIntegerField()
    net_weight = models.DecimalField(max_digits=20, decimal_places=4)
    last_cost_update = models.DateField()


class TaxProvince(models.Model):
    name = models.CharField(max_length=30)

    
class Location(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50, unique=True)
    address_1 = models.CharField(max_length=40)
    address_2 = models.CharField(max_length=40, blank=True)
    address_3 = models.CharField(max_length=40, blank=True)
    address_4 = models.CharField(max_length=40, blank=True)
    address_5 = models.CharField(max_length=40, blank=True)
    address_6 = models.CharField(max_length=40, blank=True)
    telephone = models.CharField(max_length=30)
    fax = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=30)
    tax_province = models.ForeignKey(TaxProvince)
    cash_sale_customer = models.CharField(max_length=10)
    managed = models.IntegerField()
    cash_sale_branch = models.CharField(max_length=10)
    internal_request = models.BooleanField()


class WorkCentre(models.Model):
    code = models.CharField(max_length=5, unique=True)
    location = models.ForeignKey(Location)
    description = models.CharField(max_length=20)
    capacity = models.FloatField()
    overhead_per_hour = models.DecimalField(max_digits=10, decimal_places=0)
    overhead_recovery_account = models.IntegerField()
    setup_hours = models.DecimalField(max_digits=10, decimal_places=0)


class BillOfMaterial(models.Model):
    parent = models.ForeignKey(Item)
    component = models.ForeignKey(Item)
    work_centre_added = models.ForeignKey(WorkCentre)
    location = models.ForeignKey(Location)
    effective_after = models.DateField()
    effective_to = models.DateField()
    quantity = models.FloatField()
    auto_issue = models.BooleanField()
    
    class Meta:
        unique_together = ["parent", "component", "work_centre_added", "location"]


class ChartMaster(models.Model):
    account_code = models.CharField(max_length=20, unique=True)
    account_name = models.CharField(max_length=50)
    group = models.ForeignKey(AccountGroup)
    
    def __unicode__(self):
        return self.account_code


class Period(models.Model):
    no = models.SmallIntegerField(unique=True)
    last_date_in_period = models.DateField()
    
    def __unicode__(self):
        return self.no


class ChartDetail(models.Model):
    account_code = models.ForeignKey(ChartMaster)
    period = models.ForeignKey(Period)
    budget = models.FloatField()
    actual = models.FloatField()
    bfwd = models.FloatField()
    bfwdbudget = models.FloatField()
    
    class Meta:
        unique_together = ["account_code", "period"]
    
    def __unicode__(self):
        return "%s %s" % (self.account.code, self.period)


class COGSGLPosting(models.Model):
    area = models.CharField(max_length=3)
    stk_cat = models.CharField(max_length=6)
    gl_code = models.IntegerField()
    sales_type = models.CharField(max_length=2)
    
    class Meta:
        unique_together = ["area", "stk_cat", "sales_type"]
    
    def __unicode__(self):
        return "%s %s %s" % (self.area, self.stk_cat, self.sales_type)


class Company(models.Model):
    name = models.CharField(max_length=50)
    gst_no = models.CharField(max_length=20)
    company_number = models.CharField(max_length=20)
    reg_office_1 = models.CharField(max_length=40)
    reg_office_2 = models.CharField(max_length=40)
    reg_office_3 = models.CharField(max_length=40)
    reg_office_4 = models.CharField(max_length=40)
    reg_office_5 = models.CharField(max_length=40)
    reg_office_6 = models.CharField(max_length=40)
    telephone = models.CharField(max_length=25)
    fax = models.CharField(max_length=25)
    email = models.EmailField()
    currency_default = models.CharField(max_length=4)
    debtors_act = models.IntegerField()
    pyt_discount_act = models.IntegerField()
    creditors_act = models.IntegerField()
    payroll_act = models.IntegerField()
    grn_act = models.IntegerField()
    exchange_diff_act = models.IntegerField()
    purchases_exchange_diff_act = models.IntegerField()
    retained_earnings = models.IntegerField()
    gl_link_debtors = models.SmallIntegerField()
    gl_link_creditors = models.SmallIntegerField()
    gl_link_stock = models.SmallIntegerField()
    freight_act = models.IntegerField()
    
    def __unicode__(self):
        return self.id


class Config(models.Model):
    name = models.CharField(max_length=35, unique=True)
    value = models.TextField()
    
    def __unicode__(self):
        return self.name


class ContractBOM(models.Model):
    ref = models.CharField(max_length=20)
    stock = models.ForeignKey(StockMaster)
    work_centre_added = models.ForeignKey(WorkCentre)
    quantity = models.FloatField()
    
    class Meta:
        unique_together = ["ref", "stock", "work_centre_added"]
    
    def __unicode__(self):
        return "%s %s %s" % (self.ref, self.stock, self.work_centre_added)


class HoldReasons(models.Model):
    code = models.SmallIntegerField(unique=True)
    description = models.CharField(max_length=30)
    disallow_invoices = models.BooleanField()
    
    def __unicode__(self):
        return self.code


class Currency(models.Model):
    pass


class DebtorMaster(model.Model):
    pass


class CustBranch(models.Model):
    pass


class Contract(models.Model):
    pass


class ContractCharge(models.Model):
    pass
