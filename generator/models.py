# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessLog(models.Model):
    access_log_id = models.BigAutoField(primary_key=True)
    operator = models.ForeignKey('Operator', models.DO_NOTHING, db_column='operator')
    access_agent = models.CharField(max_length=250, blank=True, null=True)
    ip_address = models.CharField(max_length=250, blank=True, null=True)
    token = models.ForeignKey('ApiToken', models.DO_NOTHING, db_column='token', blank=True, null=True)
    activity = models.CharField(max_length=250, blank=True, null=True)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'access_log'


class AccountEntryType(models.Model):
    account_entry_type_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_entry_type'


class ActivityLog(models.Model):
    activity_log_id = models.BigAutoField(primary_key=True)
    operator = models.ForeignKey('Operator', models.DO_NOTHING, db_column='operator')
    access_log = models.ForeignKey(AccessLog, models.DO_NOTHING, db_column='access_log', blank=True, null=True)
    token = models.ForeignKey('ApiToken', models.DO_NOTHING, db_column='token', blank=True, null=True)
    activity = models.TextField(blank=True, null=True)
    activity_time = models.DateTimeField(blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_log'


class AgencyCommission(models.Model):
    agency_commission_id = models.AutoField(primary_key=True)
    min_amount = models.FloatField()
    max_amount = models.FloatField()
    commission = models.FloatField()
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agency_commission'


class AgentCreditLine(models.Model):
    agent_credit_line_id = models.AutoField(primary_key=True)
    agent = models.ForeignKey('CountyAgent', models.DO_NOTHING, db_column='agent')
    credit_line = models.FloatField()
    used_float = models.CharField(max_length=250)
    float_balance = models.CharField(max_length=250)
    financial_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='financial_year')
    loaded_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='loaded_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_credit_line'


class AgentPayment(models.Model):
    agent_payment_id = models.BigAutoField(primary_key=True)
    agent = models.ForeignKey('CountyAgent', models.DO_NOTHING, db_column='agent')
    invoice = models.ForeignKey('InvoiceControl', models.DO_NOTHING, db_column='invoice')
    amount = models.FloatField()
    txn_code = models.CharField(max_length=250)
    received_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='received_by')
    financial_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='financial_year')
    is_trashed = models.IntegerField(blank=True, null=True)
    received_on = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_payment'


class AgentTxn(models.Model):
    agent_txn_id = models.BigAutoField(primary_key=True)
    agent = models.ForeignKey('CountyAgent', models.DO_NOTHING, db_column='agent')
    received_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='received_by')
    invoice = models.ForeignKey('InvoiceControl', models.DO_NOTHING, db_column='invoice')
    citizen_bill = models.ForeignKey('Billing', models.DO_NOTHING, db_column='citizen_bill')
    amount_paid = models.FloatField()
    commission_applied = models.FloatField()
    commission = models.FloatField()
    financial_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='financial_year')
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_txn'


class ApiApp(models.Model):
    api_app_id = models.AutoField(primary_key=True)
    app_key = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_app'


class ApiToken(models.Model):
    api_token_id = models.BigAutoField(primary_key=True)
    api_user = models.ForeignKey('ApiUser', models.DO_NOTHING, db_column='api_user', blank=True, null=True)
    operator = models.ForeignKey('Operator', models.DO_NOTHING, db_column='operator', blank=True, null=True)
    token = models.CharField(max_length=250, blank=True, null=True)
    pos_device = models.ForeignKey('PosDevice', models.DO_NOTHING, db_column='pos_device', blank=True, null=True)
    generated_on = models.DateTimeField(blank=True, null=True)
    expire_on = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_token'


class ApiUser(models.Model):
    api_user_id = models.AutoField(primary_key=True)
    api_app = models.ForeignKey(ApiApp, models.DO_NOTHING, db_column='api_app')
    api_username = models.CharField(max_length=250)
    api_userpass = models.CharField(max_length=250)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_user'


class ArrearsAudit(models.Model):
    arrears_audit_id = models.BigAutoField(primary_key=True)
    financial_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='financial_year', blank=True,
                                       null=True)
    entry_type = models.ForeignKey(AccountEntryType, models.DO_NOTHING, db_column='entry_type', blank=True, null=True)
    arrear_month = models.CharField(max_length=250, blank=True, null=True)
    arrears_account = models.ForeignKey('PropertyArrears', models.DO_NOTHING, db_column='arrears_account', blank=True,
                                        null=True)
    principal_amount = models.FloatField(blank=True, null=True)
    accrued_intrest = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    initiated_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='initiated_by', blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arrears_audit'


class BankBranch(models.Model):
    bank_branch_id = models.AutoField(primary_key=True)
    bank = models.ForeignKey('CountyBank', models.DO_NOTHING, db_column='bank')
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_branch'


class BankPayment(models.Model):
    bank_payment_id = models.BigAutoField(primary_key=True)
    bank = models.ForeignKey('CountyBank', models.DO_NOTHING, db_column='bank')
    branch = models.ForeignKey(BankBranch, models.DO_NOTHING, db_column='branch')
    account = models.ForeignKey('CountyAccount', models.DO_NOTHING, db_column='account')
    payment_type = models.ForeignKey('BankPaymentType', models.DO_NOTHING, db_column='payment_type', blank=True,
                                     null=True)
    txn_code = models.CharField(max_length=250)
    invoice = models.ForeignKey('InvoiceControl', models.DO_NOTHING, db_column='invoice')
    amount = models.FloatField()
    is_legit = models.IntegerField(blank=True, null=True)
    financial_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='financial_year')
    received_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='received_by')
    transaction_number = models.CharField(max_length=250, blank=True, null=True)
    cheque = models.ForeignKey('ChequePayment', models.DO_NOTHING, db_column='cheque', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_payment'


class BankPaymentType(models.Model):
    bank_payment_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_payment_type'


class BillAuditTrail(models.Model):
    bill_audit_trail_id = models.BigAutoField(primary_key=True)
    citizen_bill = models.ForeignKey('Billing', models.DO_NOTHING, db_column='citizen_bill')
    description = models.CharField(max_length=250)
    citizen_account = models.ForeignKey('CitizenAccount', models.DO_NOTHING, db_column='citizen_account', blank=True,
                                        null=True)
    payment = models.ForeignKey('Payment', models.DO_NOTHING, db_column='payment', blank=True, null=True)
    logged_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='logged_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    audit_trailed_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bill_audit_trail'


class BillItem(models.Model):
    bill_item_id = models.BigAutoField(primary_key=True)
    citizen_bill = models.ForeignKey('Billing', models.DO_NOTHING, db_column='citizen_bill')
    revenue_source = models.ForeignKey('RevenueSource', models.DO_NOTHING, db_column='revenue_source', blank=True,
                                       null=True)
    revenue_type = models.ForeignKey('RevenueType', models.DO_NOTHING, db_column='revenue_type', blank=True, null=True)
    revenue_category = models.ForeignKey('RevenueCategory', models.DO_NOTHING, db_column='revenue_category', blank=True,
                                         null=True)
    revenue_subcategory = models.ForeignKey('RevenueSubcategory', models.DO_NOTHING, db_column='revenue_subcategory',
                                            blank=True, null=True)
    business_category = models.ForeignKey('BusinessCategory', models.DO_NOTHING, db_column='business_category',
                                          blank=True, null=True)
    business_subcategory = models.ForeignKey('BusinessSubcategory', models.DO_NOTHING, db_column='business_subcategory',
                                             blank=True, null=True)
    parcel_category = models.ForeignKey('ParcelCategory', models.DO_NOTHING, db_column='parcel_category', blank=True,amount
                                        null=True)
    county_property = models.ForeignKey('CountyProperty', models.DO_NOTHING, db_column='county_property', blank=True,
                                        null=True)
    county_property_category = models.ForeignKey('CountyPropertyCategory', models.DO_NOTHING,
                                                 db_column='county_property_category', blank=True, null=True)
    unit_of_measure = models.ForeignKey('UnitOfMeasure', models.DO_NOTHING, db_column='unit_of_measure', blank=True,
                                        null=True)
    quantity = models.FloatField(blank=True, null=True)
    unit_amount = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    serial_code = models.CharField(max_length=250, blank=True, null=True)
    initiated_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='initiated_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_item'


class BillPayment(models.Model):
    bill_payment_id = models.BigAutoField(primary_key=True)
    payment = models.ForeignKey('Payment', models.DO_NOTHING, db_column='payment')
    citizen_bill = models.ForeignKey('Billing', models.DO_NOTHING, db_column='citizen_bill')
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_payment'


class BillPenalty(models.Model):
    bill_penalty_id = models.BigAutoField(primary_key=True)
    bill = models.ForeignKey('Billing', models.DO_NOTHING, db_column='bill', blank=True, null=True)
    penalty = models.ForeignKey('PenaltyConfig', models.DO_NOTHING, db_column='penalty', blank=True, null=True)
    penalty_amount = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    payment_status = models.ForeignKey('PaymentStatus', models.DO_NOTHING, db_column='payment_status', blank=True,
                                       null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    penalized_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_penalty'


class BillSource(models.Model):
    bill_source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_source'


class Billing(models.Model):
    billing_id = models.BigAutoField(primary_key=True)
    invoice = models.ForeignKey('InvoiceControl', models.DO_NOTHING, db_column='invoice')
    bill_source = models.ForeignKey(BillSource, models.DO_NOTHING, db_column='bill_source')
    financial_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='financial_year')
    citizen = models.ForeignKey('Citizen', models.DO_NOTHING, db_column='citizen', blank=True, null=True)
    amount = models.FloatField()
    penalty = models.FloatField(blank=True, null=True)
    bill_amount = models.FloatField(blank=True, null=True)
    discount_authorized_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='discount_authorized_by',
                                               blank=True, null=True)
    discount_percent = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    paid_amount = models.FloatField()
    balance = models.FloatField()
    payment_status = models.ForeignKey('PaymentStatus', models.DO_NOTHING, db_column='payment_status')
    business = models.ForeignKey('Business', models.DO_NOTHING, db_column='business', blank=True, null=True)
    land_parcel = models.ForeignKey('LandParcel', models.DO_NOTHING, db_column='land_parcel', blank=True, null=True)
    county_property_unit = models.ForeignKey('CountyPropertyUnit', models.DO_NOTHING, db_column='county_property_unit',
                                             blank=True, null=True)
    vehicle_parking = models.ForeignKey('VehicleParking', models.DO_NOTHING, db_column='vehicle_parking', blank=True,
                                        null=True)
    generated_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='generated_by')
    comment = models.CharField(max_length=250, blank=True, null=True)
    organization = models.ForeignKey('Organization', models.DO_NOTHING, db_column='organization')
    county = models.ForeignKey('County', models.DO_NOTHING, db_column='county')
    sub_county = models.ForeignKey('SubCounty', models.DO_NOTHING, db_column='sub_county', blank=True, null=True)
    ward = models.ForeignKey('Ward', models.DO_NOTHING, db_column='ward', blank=True, null=True)
    collection_center = models.ForeignKey('CollectionCenters', models.DO_NOTHING, db_column='collection_center',
                                          blank=True, null=True)
    collector_pos_device = models.ForeignKey('PosDevice', models.DO_NOTHING, db_column='collector_pos_device',
                                             blank=True, null=True)
    txn_date = models.DateTimeField(blank=True, null=True)
    citizen_name = models.CharField(max_length=250, blank=True, null=True)
    citizen_mobile = models.CharField(max_length=250, blank=True, null=True)
    bill_narration = models.CharField(max_length=250, blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    generated_on = models.DateTimeField(blank=True, null=True)
    cleared_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing'


class Business(models.Model):
    business_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    business_number = models.CharField(max_length=250)
    postal_addresss = models.CharField(max_length=250, blank=True, null=True)
    physical_address = models.CharField(max_length=250, blank=True, null=True)
    plot_number = models.CharField(max_length=250, blank=True, null=True)
    building = models.CharField(max_length=250, blank=True, null=True)
    business_activity = models.TextField(blank=True, null=True)
    business_category = models.ForeignKey('BusinessCategory', models.DO_NOTHING, db_column='business_category')
    business_subcategory = models.ForeignKey('BusinessSubcategory', models.DO_NOTHING, db_column='business_subcategory')
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone')
    business_size = models.ForeignKey('BusinessSize', models.DO_NOTHING, db_column='business_size')
    sub_county = models.ForeignKey('SubCounty', models.DO_NOTHING, db_column='sub_county')
    ward = models.ForeignKey('Ward', models.DO_NOTHING, db_column='ward')
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business'


class BusinessCategory(models.Model):
    business_category_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=250)
    name = models.TextField()
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_category'


class BusinessLicence(models.Model):
    business_licence_id = models.BigAutoField(primary_key=True)
    business = models.ForeignKey(Business, models.DO_NOTHING, db_column='business')
    licence_type = models.ForeignKey('LicenseType', models.DO_NOTHING, db_column='licence_type', blank=True, null=True)
    permit_number = models.CharField(max_length=250)
    financial_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='financial_year')
    issued_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='issued_by')
    validity_token = models.CharField(max_length=250)
    valid_from = models.DateField()
    valid_until = models.DateField()
    bill_info = models.ForeignKey(Billing, models.DO_NOTHING, db_column='bill_info')
    invoice = models.ForeignKey('InvoiceControl', models.DO_NOTHING, db_column='invoice')
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_licence'


class BusinessSize(models.Model):
    business_size_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_size'


class BusinessSubcategory(models.Model):
    business_subcategory_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=250)
    name = models.TextField()
    business_category = models.ForeignKey(BusinessCategory, models.DO_NOTHING, db_column='business_category')
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_subcategory'


class BusparkMatatu(models.Model):
    buspark_matatu_id = models.BigAutoField(primary_key=True)
    citizen = models.ForeignKey('Citizen', models.DO_NOTHING, db_column='citizen', blank=True, null=True)
    sacco = models.ForeignKey('BusparkSacco', models.DO_NOTHING, db_column='sacco', blank=True, null=True)
    registration_number = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buspark_matatu'


class BusparkSacco(models.Model):
    buspark_sacco_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buspark_sacco'


class CashPayment(models.Model):
    cash_payment_id = models.BigAutoField(primary_key=True)
    invoice = models.ForeignKey('InvoiceControl', models.DO_NOTHING, db_column='invoice')
    amount = models.FloatField()
    txn_code = models.CharField(max_length=250)
    received_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='received_by')
    financial_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='financial_year')
    is_trashed = models.IntegerField(blank=True, null=True)
    received_on = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_payment'


class ChartOfAccount(models.Model):
    chart_of_account_id = models.AutoField(primary_key=True)
    gl_code = models.CharField(max_length=250)
    gl_name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chart_of_account'


class ChequePayment(models.Model):
    cheque_payment_id = models.BigAutoField(primary_key=True)
    cheque_number = models.CharField(max_length=250)
    drawer = models.CharField(max_length=250)
    tt_number = models.CharField(max_length=250)
    bank = models.CharField(max_length=250)
    amount = models.FloatField(blank=True, null=True)
    is_cleared = models.IntegerField(blank=True, null=True)
    txn_ref_number = models.CharField(max_length=250, blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    received_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='received_by', blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheque_payment'


class Citizen(models.Model):
    citizen_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    id_type = models.ForeignKey('IdType', models.DO_NOTHING, db_column='id_type')
    id_number = models.CharField(max_length=250, blank=True, null=True)
    kra_pin = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.ForeignKey('Country', models.DO_NOTHING, db_column='nationality')
    is_county_resident = models.IntegerField(blank=True, null=True)
    county = models.ForeignKey('County', models.DO_NOTHING, db_column='county', blank=True, null=True)
    sub_county = models.ForeignKey('SubCounty', models.DO_NOTHING, db_column='sub_county', blank=True, null=True)
    ward = models.ForeignKey('Ward', models.DO_NOTHING, db_column='ward', blank=True, null=True)
    allow_system_access = models.IntegerField(blank=True, null=True)
    create_wallet_account = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizen'


class CitizenAccount(models.Model):
    citizen_account_id = models.BigAutoField(primary_key=True)
    account_summary = models.ForeignKey('CitizenAccountSummary', models.DO_NOTHING, db_column='account_summary',
                                        blank=True, null=True)
    citizen = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='citizen')
    entry_type = models.ForeignKey(AccountEntryType, models.DO_NOTHING, db_column='entry_type', blank=True, null=True)
    entry_description = models.CharField(max_length=300, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    bill_reference = models.ForeignKey(Billing, models.DO_NOTHING, db_column='bill_reference', blank=True, null=True)
    payment_reference = models.ForeignKey('Payment', models.DO_NOTHING, db_column='payment_reference', blank=True,
                                          null=True)
    txn_date = models.DateTimeField(blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizen_account'


class CitizenAccountSummary(models.Model):
    citizen_account_summary_id = models.BigAutoField(primary_key=True)
    citizen = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='citizen', blank=True, null=True)
    cumulated_amount = models.FloatField(blank=True, null=True)
    cumulated_cleared = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizen_account_summary'


class CitizenContact(models.Model):
    citizen_contact_id = models.BigAutoField(primary_key=True)
    citizen = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='citizen')
    phone = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    postal_address = models.CharField(max_length=250, blank=True, null=True)
    physical_address = models.CharField(max_length=250, blank=True, null=True)
    is_primay_contact = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizen_contact'


class CitizenObligation(models.Model):
    citizen_obligation_id = models.BigAutoField(primary_key=True)
    citizen = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='citizen')
    financial_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='financial_year')
    business = models.ForeignKey(Business, models.DO_NOTHING, db_column='business', blank=True, null=True)
    land_parcel = models.ForeignKey('LandParcel', models.DO_NOTHING, db_column='land_parcel', blank=True, null=True)
    county_propery_unit = models.ForeignKey('CountyPropertyUnit', models.DO_NOTHING, db_column='county_propery_unit',
                                            blank=True, null=True)
    obligation_period = models.ForeignKey('ObligationPeriod', models.DO_NOTHING, db_column='obligation_period')
    initiated_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='initiated_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizen_obligation'


class CitizenObligationItem(models.Model):
    citizen_obligation_item_id = models.BigAutoField(primary_key=True)
    citizen_obligation = models.ForeignKey(CitizenObligation, models.DO_NOTHING, db_column='citizen_obligation')
    revenue_source = models.ForeignKey('RevenueSource', models.DO_NOTHING, db_column='revenue_source', blank=True,
                                       null=True)
    revenue_category = models.ForeignKey('RevenueCategory', models.DO_NOTHING, db_column='revenue_category', blank=True,
                                         null=True)
    revenue_subcategory = models.ForeignKey('RevenueSubcategory', models.DO_NOTHING, db_column='revenue_subcategory',
                                            blank=True, null=True)
    business_category = models.ForeignKey(BusinessCategory, models.DO_NOTHING, db_column='business_category',
                                          blank=True, null=True)
    business_subcategory = models.ForeignKey(BusinessSubcategory, models.DO_NOTHING, db_column='business_subcategory',
                                             blank=True, null=True)
    parcel_category = models.ForeignKey('ParcelCategory', models.DO_NOTHING, db_column='parcel_category', blank=True,
                                        null=True)
    county_property_category = models.ForeignKey('CountyPropertyCategory', models.DO_NOTHING,
                                                 db_column='county_property_category', blank=True, null=True)
    county_property = models.ForeignKey('CountyProperty', models.DO_NOTHING, db_column='county_property', blank=True,
                                        null=True)
    unit_of_measure = models.ForeignKey('UnitOfMeasure', models.DO_NOTHING, db_column='unit_of_measure', blank=True,
                                        null=True)
    is_renewable = models.IntegerField(blank=True, null=True)
    initiated_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='initiated_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizen_obligation_item'


class ClearanceAccount(models.Model):
    clearance_account_id = models.BigAutoField(primary_key=True)
    clearance_account_summary = models.ForeignKey('ClearanceAccountSummary', models.DO_NOTHING,
                                                  db_column='clearance_account_summary', blank=True, null=True)
    financial_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='financial_year', blank=True,
                                       null=True)
    collector = models.ForeignKey('Operator', models.DO_NOTHING, db_column='collector', blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    cleared_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='cleared_by', blank=True, null=True)
    txn_code = models.CharField(max_length=250, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    collection_center = models.ForeignKey('CollectionCenters', models.DO_NOTHING, db_column='collection_center',
                                          blank=True, null=True)
    cleared_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clearance_account'


class ClearanceAccountSummary(models.Model):
    clearance_account_summary_id = models.AutoField(primary_key=True)
    clearing_officer = models.ForeignKey('Operator', models.DO_NOTHING, db_column='clearing_officer', blank=True,
                                         null=True)
    cummulated_cleared_amount = models.FloatField(blank=True, null=True)
    cummulated_banked_amount = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    updated_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='updated_by', blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clearance_account_summary'


class CollectionBanking(models.Model):
    collection_banking_id = models.BigAutoField(primary_key=True)
    financial_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='financial_year', blank=True,
                                       null=True)
    collector = models.ForeignKey('Operator', models.DO_NOTHING, db_column='collector', blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    reference_number = models.CharField(max_length=250, blank=True, null=True)
    bank = models.ForeignKey('CountyBank', models.DO_NOTHING, db_column='bank', blank=True, null=True)
    branch = models.ForeignKey(BankBranch, models.DO_NOTHING, db_column='branch', blank=True, null=True)
    account = models.ForeignKey('CountyAccount', models.DO_NOTHING, db_column='account', blank=True, null=True)
    deposited_on = models.DateField(blank=True, null=True)
    posted_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='posted_by', blank=True, null=True)
    posted_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection_banking'


class CollectionCenters(models.Model):
    collection_centers_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    ward = models.ForeignKey('Ward', models.DO_NOTHING, db_column='ward')
    is_trashed = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection_centers'


class CollectorAccount(models.Model):
    collector_account_id = models.BigAutoField(primary_key=True)
    account_summary = models.ForeignKey('CollectorAccountSummary', models.DO_NOTHING, db_column='account_summary',
                                        blank=True, null=True)
    txn_code = models.CharField(max_length=250, blank=True, null=True)
    collector = models.ForeignKey('Operator', models.DO_NOTHING, db_column='collector')
    entry_type = models.ForeignKey(AccountEntryType, models.DO_NOTHING, db_column='entry_type', blank=True, null=True)
    entry_description = models.CharField(max_length=300, blank=True, null=True)
    bill_reference = models.ForeignKey(Billing, models.DO_NOTHING, db_column='bill_reference', blank=True, null=True)
    payment_reference = models.ForeignKey('Payment', models.DO_NOTHING, db_column='payment_reference', blank=True,
                                          null=True)
    txn_date = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    cumulated_amount = models.FloatField(blank=True, null=True)
    cumulated_balance = models.FloatField(blank=True, null=True)
    cumulated_cleared_amount = models.FloatField(blank=True, null=True)
    effected_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='effected_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collector_account'


class CollectorAccountSummary(models.Model):
    collector_account_summary_id = models.AutoField(primary_key=True)
    collector = models.ForeignKey('Operator', models.DO_NOTHING, db_column='collector', blank=True, null=True)
    cumulated_amount = models.FloatField(blank=True, null=True)
    cumulated_cleared_amount = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    updated_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='updated_by', blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collector_account_summary'


class CollectorLocation(models.Model):
    collector_location_id = models.BigAutoField(primary_key=True)
    collector = models.ForeignKey('Operator', models.DO_NOTHING, db_column='collector', blank=True, null=True)
    collection_center = models.ForeignKey(CollectionCenters, models.DO_NOTHING, db_column='collection_center',
                                          blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    transfered_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='transfered_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    transfered_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collector_location'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class County(models.Model):
    county_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county'


class CountyAccount(models.Model):
    county_account_id = models.AutoField(primary_key=True)
    bank = models.ForeignKey('CountyBank', models.DO_NOTHING, db_column='bank')
    branch = models.ForeignKey(BankBranch, models.DO_NOTHING, db_column='branch')
    account_number = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county_account'


class CountyAgent(models.Model):
    county_agent_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    registration_number = models.CharField(max_length=250)
    kra_pin_number = models.CharField(max_length=250)
    sub_county = models.ForeignKey('SubCounty', models.DO_NOTHING, db_column='sub_county')
    ward = models.ForeignKey('Ward', models.DO_NOTHING, db_column='ward')
    physical_address = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    postal_address = models.CharField(max_length=250)
    apply_flat_commission = models.IntegerField(blank=True, null=True)
    commission = models.FloatField(blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county_agent'


class CountyBank(models.Model):
    county_bank_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county_bank'


class CountyProperty(models.Model):
    county_rent_id = models.AutoField(primary_key=True)
    property_category = models.ForeignKey('CountyPropertyCategory', models.DO_NOTHING, db_column='property_category')
    name = models.CharField(max_length=250)
    sub_county = models.ForeignKey('SubCounty', models.DO_NOTHING, db_column='sub_county')
    ward = models.ForeignKey('Ward', models.DO_NOTHING, db_column='ward')
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county_property'


class CountyPropertyCategory(models.Model):
    county_property_category_id = models.AutoField(primary_key=True)
    revenue_source = models.ForeignKey('RevenueSource', models.DO_NOTHING, db_column='revenue_source')
    name = models.CharField(max_length=250)
    pos_enabled = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county_property_category'


class CountyPropertyCostMatrix(models.Model):
    county_property_cost_matrix_id = models.BigAutoField(primary_key=True)
    financial_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='financial_year')
    county_property_category = models.ForeignKey(CountyPropertyCategory, models.DO_NOTHING,
                                                 db_column='county_property_category')
    county_property = models.ForeignKey(CountyProperty, models.DO_NOTHING, db_column='county_property')
    unit_of_measure = models.ForeignKey('UnitOfMeasure', models.DO_NOTHING, db_column='unit_of_measure', blank=True,
                                        null=True)
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone', blank=True, null=True)
    cost = models.FloatField()
    is_current = models.IntegerField(blank=True, null=True)
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county_property_cost_matrix'


class CountyPropertyUnit(models.Model):
    county_property_unit_id = models.AutoField(primary_key=True)
    county_property = models.ForeignKey(CountyProperty, models.DO_NOTHING, db_column='county_property')
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    unit_size = models.ForeignKey('UnitOfMeasure', models.DO_NOTHING, db_column='unit_size')

    class Meta:
        managed = False
        db_table = 'county_property_unit'


class FinancialYear(models.Model):
    financial_year_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    start_on = models.DateTimeField()
    end_on = models.DateTimeField()
    is_current = models.IntegerField(blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financial_year'


class IdType(models.Model):
    id_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'id_type'


class InvoiceControl(models.Model):
    invoice_id = models.BigAutoField(primary_key=True)
    financial_year = models.ForeignKey(FinancialYear, models.DO_NOTHING, db_column='financial_year')
    long_name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=200)
    initiated_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='initiated_by')
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_control'


class LandParcel(models.Model):
    land_parcel_id = models.AutoField(primary_key=True)
    parcel_category = models.ForeignKey('ParcelCategory', models.DO_NOTHING, db_column='parcel_category')
    parcel_number = models.CharField(max_length=250)
    parcel_size = models.FloatField(blank=True, null=True)
    geo_location = models.TextField(blank=True, null=True)
    sub_county = models.ForeignKey('SubCounty', models.DO_NOTHING, db_column='sub_county')
    ward = models.ForeignKey('Ward', models.DO_NOTHING, db_column='ward')
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone')
    net_annual_value = models.FloatField(blank=True, null=True)
    land_rent_amount = models.FloatField(blank=True, null=True)
    valuation_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'land_parcel'


class LicenseType(models.Model):
    license_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'license_type'


class MobileChannel(models.Model):
    mobile_channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mobile_channel'


class MobilePayment(models.Model):
    mobile_payment_id = models.BigAutoField(primary_key=True)
    mobile_channel = models.ForeignKey(MobileChannel, models.DO_NOTHING, db_column='mobile_channel')
    sender_name = models.CharField(max_length=250)
    sender_phone = models.CharField(max_length=250)
    amount = models.FloatField()
    txn_ref_number = models.CharField(max_length=250, blank=True, null=True)
    ref_account_number = models.CharField(max_length=250, blank=True, null=True)
    financial_year = models.ForeignKey(FinancialYear, models.DO_NOTHING, db_column='financial_year')
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mobile_payment'


class NotificationSettings(models.Model):
    settings_id = models.AutoField(primary_key=True)
    sms_user = models.CharField(max_length=250)
    sms_passcode = models.IntegerField()
    sms_key = models.CharField(max_length=250)
    email_name = models.CharField(max_length=250)
    email_passcode = models.CharField(max_length=250)
    global_notify = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_settings'


class ObligationPeriod(models.Model):
    obligation_period_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey('Operator', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obligation_period'


class Operator(models.Model):
    operator_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)
    passcode = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    email = models.CharField(max_length=250, blank=True, null=True)
    user_type = models.ForeignKey('UserType', models.DO_NOTHING, db_column='user_type', blank=True, null=True)
    organization = models.ForeignKey('Organization', models.DO_NOTHING, db_column='organization', blank=True, null=True)
    role_center = models.ForeignKey('RoleCenter', models.DO_NOTHING, db_column='role_center', blank=True, null=True)
    agent = models.ForeignKey(CountyAgent, models.DO_NOTHING, db_column='agent', blank=True, null=True)
    citizen = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='citizen', blank=True, null=True)
    user_status = models.ForeignKey('UserStatus', models.DO_NOTHING, db_column='user_status', blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operator'


class Organization(models.Model):
    organization_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    category = models.ForeignKey('OrganizationCategory', models.DO_NOTHING, db_column='category')
    organization_parent = models.IntegerField()
    county = models.ForeignKey(County, models.DO_NOTHING, db_column='county', blank=True, null=True)
    sub_county = models.ForeignKey('SubCounty', models.DO_NOTHING, db_column='sub_county', blank=True, null=True)
    ward = models.ForeignKey('Ward', models.DO_NOTHING, db_column='ward', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    update_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization'


class OrganizationAction(models.Model):
    organization_action_id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization')
    action = models.ForeignKey('ResourceAction', models.DO_NOTHING, db_column='action')
    resource = models.ForeignKey('Resource', models.DO_NOTHING, db_column='resource')
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    update_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization_action'


class OrganizationCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization_category'


class OtherBusinessFee(models.Model):
    associated_fee_id = models.BigAutoField(primary_key=True)
    business = models.ForeignKey(Business, models.DO_NOTHING, db_column='business', blank=True, null=True)
    revenue_source = models.ForeignKey('RevenueSource', models.DO_NOTHING, db_column='revenue_source')
    revenue_category = models.ForeignKey('RevenueCategory', models.DO_NOTHING, db_column='revenue_category')
    revenue_subcategory = models.ForeignKey('RevenueSubcategory', models.DO_NOTHING, db_column='revenue_subcategory')
    unit_of_measure = models.ForeignKey('UnitOfMeasure', models.DO_NOTHING, db_column='unit_of_measure')
    is_renewable = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_business_fee'


class ParcelCategory(models.Model):
    parcel_category_id = models.AutoField(primary_key=True)
    revenue_source = models.ForeignKey('RevenueSource', models.DO_NOTHING, db_column='revenue_source')
    name = models.CharField(max_length=250)
    pos_enabled = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_category'


class ParcelCostMatrix(models.Model):
    parcel_cost_matrix_id = models.BigAutoField(primary_key=True)
    financial_year = models.ForeignKey(FinancialYear, models.DO_NOTHING, db_column='financial_year')
    parcel_category = models.ForeignKey(ParcelCategory, models.DO_NOTHING, db_column='parcel_category')
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone')
    cost = models.FloatField()
    is_current = models.IntegerField(blank=True, null=True)
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_cost_matrix'


class Payment(models.Model):
    payment_id = models.BigAutoField(primary_key=True)
    amount = models.FloatField()
    receipt_number = models.CharField(max_length=250)
    channel = models.ForeignKey('PaymentChannel', models.DO_NOTHING, db_column='channel')
    invoice = models.ForeignKey(InvoiceControl, models.DO_NOTHING, db_column='invoice')
    financial_year = models.ForeignKey(FinancialYear, models.DO_NOTHING, db_column='financial_year')
    collection_center = models.ForeignKey(CollectionCenters, models.DO_NOTHING, db_column='collection_center',
                                          blank=True, null=True)
    collector_pos = models.ForeignKey('PosDevice', models.DO_NOTHING, db_column='collector_pos', blank=True, null=True)
    mobile_payment = models.ForeignKey(MobilePayment, models.DO_NOTHING, db_column='mobile_payment', blank=True,
                                       null=True)
    bank_payment = models.ForeignKey(BankPayment, models.DO_NOTHING, db_column='bank_payment', blank=True, null=True)
    cash_payment = models.ForeignKey(CashPayment, models.DO_NOTHING, db_column='cash_payment', blank=True, null=True)
    agent_payment = models.ForeignKey(AgentPayment, models.DO_NOTHING, db_column='agent_payment', blank=True, null=True)
    wallet_payment = models.ForeignKey('WalletPayment', models.DO_NOTHING, db_column='wallet_payment', blank=True,
                                       null=True)
    processed_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='processed_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    received_on = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class PaymentAuditTrail(models.Model):
    payment_audit_trail_id = models.BigAutoField(primary_key=True)
    payment = models.ForeignKey(Payment, models.DO_NOTHING, db_column='payment')
    description = models.CharField(max_length=250)
    citizen_account = models.ForeignKey(CitizenAccount, models.DO_NOTHING, db_column='citizen_account', blank=True,
                                        null=True)
    citizen_bill = models.ForeignKey(Billing, models.DO_NOTHING, db_column='citizen_bill', blank=True, null=True)
    audit_logged_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='audit_logged_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    audit_trailed_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment_audit_trail'


class PaymentChannel(models.Model):
    payment_channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_channel'


class PaymentStatus(models.Model):
    payment_status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by')
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_status'


class PaymentTerm(models.Model):
    payment_term_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_term'


class PenaltyConfig(models.Model):
    penalty_config_id = models.AutoField(primary_key=True)
    revenue_source = models.ForeignKey('RevenueSource', models.DO_NOTHING, db_column='revenue_source')
    revenue_type = models.ForeignKey('RevenueType', models.DO_NOTHING, db_column='revenue_type', blank=True, null=True)
    financial_year = models.ForeignKey(FinancialYear, models.DO_NOTHING, db_column='financial_year')
    start_date = models.DateField()
    end_date = models.DateField()
    penalty_percent = models.FloatField()
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'penalty_config'


class PermitCostMatrix(models.Model):
    permit_cost_matrix_id = models.BigAutoField(primary_key=True)
    financial_year = models.ForeignKey(FinancialYear, models.DO_NOTHING, db_column='financial_year')
    business_category = models.ForeignKey(BusinessCategory, models.DO_NOTHING, db_column='business_category')
    business_subcategory = models.ForeignKey(BusinessSubcategory, models.DO_NOTHING, db_column='business_subcategory')
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone')
    business_size = models.ForeignKey(BusinessSize, models.DO_NOTHING, db_column='business_size')
    cost = models.FloatField()
    is_current = models.IntegerField(blank=True, null=True)
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permit_cost_matrix'


class PosAssignment(models.Model):
    device_assignment_id = models.AutoField(primary_key=True)
    operator = models.ForeignKey(Operator, models.DO_NOTHING, db_column='operator')
    pos_device = models.ForeignKey('PosDevice', models.DO_NOTHING, db_column='pos_device')
    sim_card = models.ForeignKey('SimCard', models.DO_NOTHING, db_column='sim_card')
    assigned_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='assigned_by')
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_assignment'


class PosDevice(models.Model):
    pos_device_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    imei = models.CharField(max_length=100)
    is_active = models.IntegerField(blank=True, null=True)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization')
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_device'


class PropertyArrears(models.Model):
    property_arrears_id = models.BigAutoField(primary_key=True)
    citizen = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='citizen', blank=True, null=True)
    county_property_unit = models.ForeignKey(CountyPropertyUnit, models.DO_NOTHING, db_column='county_property_unit',
                                             blank=True, null=True)
    business = models.ForeignKey(Business, models.DO_NOTHING, db_column='business', blank=True, null=True)
    land_parcel = models.ForeignKey(LandParcel, models.DO_NOTHING, db_column='land_parcel', blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    export_date = models.DateField(blank=True, null=True)
    is_billed = models.IntegerField(blank=True, null=True)
    billing = models.ForeignKey(Billing, models.DO_NOTHING, db_column='billing', blank=True, null=True)
    paid_amount = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    accrued_intrest = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    initiated_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='initiated_by', blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property_arrears'


class PropertyOwner(models.Model):
    business_owner = models.BigAutoField(primary_key=True)
    citizen = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='citizen')
    business = models.ForeignKey(Business, models.DO_NOTHING, db_column='business', blank=True, null=True)
    land_parcel = models.ForeignKey(LandParcel, models.DO_NOTHING, db_column='land_parcel', blank=True, null=True)
    county_property_unit = models.ForeignKey(CountyPropertyUnit, models.DO_NOTHING, db_column='county_property_unit',
                                             blank=True, null=True)
    is_primary = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property_owner'


class Resource(models.Model):
    resource_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=45)
    icon = models.CharField(max_length=45)
    enabled = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource'


class ResourceAction(models.Model):
    resource_action_id = models.AutoField(primary_key=True)
    resource = models.ForeignKey(Resource, models.DO_NOTHING, db_column='resource')
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=45)
    icon = models.CharField(max_length=45)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_action'


class RevenueCategory(models.Model):
    revenue_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    revenue_type = models.ForeignKey('RevenueType', models.DO_NOTHING, db_column='revenue_type')
    pos_enabled = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'revenue_category'


class RevenueCostMatrix(models.Model):
    revenue_cost_matrix_id = models.BigAutoField(primary_key=True)
    financial_year = models.ForeignKey(FinancialYear, models.DO_NOTHING, db_column='financial_year')
    revenue_category = models.ForeignKey(RevenueCategory, models.DO_NOTHING, db_column='revenue_category')
    revenue_subcategory = models.ForeignKey('RevenueSubcategory', models.DO_NOTHING, db_column='revenue_subcategory')
    unit_of_measure = models.ForeignKey('UnitOfMeasure', models.DO_NOTHING, db_column='unit_of_measure', blank=True,
                                        null=True)
    cost = models.FloatField()
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    is_current = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'revenue_cost_matrix'


class RevenueSource(models.Model):
    revenue_source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    pos_enabled = models.IntegerField(blank=True, null=True)
    general_ledger = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, db_column='general_ledger', blank=True,
                                       null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'revenue_source'


class RevenueSubcategory(models.Model):
    revenue_subcategory_id = models.AutoField(primary_key=True)
    revenue_category = models.ForeignKey(RevenueCategory, models.DO_NOTHING, db_column='revenue_category')
    name = models.CharField(max_length=250)
    pos_enabled = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'revenue_subcategory'


class RevenueType(models.Model):
    revenue_type_id = models.AutoField(primary_key=True)
    revenue_source = models.ForeignKey(RevenueSource, models.DO_NOTHING, db_column='revenue_source')
    name = models.CharField(max_length=250)
    pos_enabled = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'revenue_type'


class RoleAction(models.Model):
    role_action_id = models.BigAutoField(primary_key=True)
    role_center = models.ForeignKey('RoleCenter', models.DO_NOTHING, db_column='role_center')
    role_action = models.ForeignKey(ResourceAction, models.DO_NOTHING, db_column='role_action')
    resource = models.ForeignKey(Resource, models.DO_NOTHING, db_column='resource')
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_action'


class RoleCenter(models.Model):
    role_center_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization')
    is_active = models.IntegerField(blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_center'


class SimCard(models.Model):
    sim_card_id = models.AutoField(primary_key=True)
    sim_serial_number = models.CharField(max_length=250)
    sim_number = models.CharField(max_length=45)
    is_active = models.IntegerField(blank=True, null=True)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization')
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sim_card'


class SubCounty(models.Model):
    sub_county_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    county = models.ForeignKey(County, models.DO_NOTHING, db_column='county')
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_county'


class SuspensePayment(models.Model):
    suspense_payment_id = models.BigAutoField(primary_key=True)
    channel = models.ForeignKey(PaymentChannel, models.DO_NOTHING, db_column='channel')
    invoice = models.CharField(max_length=250, blank=True, null=True)
    mobile_payment = models.ForeignKey(MobilePayment, models.DO_NOTHING, db_column='mobile_payment', blank=True,
                                       null=True)
    bank_payment = models.ForeignKey(BankPayment, models.DO_NOTHING, db_column='bank_payment', blank=True, null=True)
    cash_payment = models.ForeignKey(CashPayment, models.DO_NOTHING, db_column='cash_payment', blank=True, null=True)
    agent_payment = models.ForeignKey(AgentPayment, models.DO_NOTHING, db_column='agent_payment', blank=True, null=True)
    wallet_payment = models.ForeignKey('WalletPayment', models.DO_NOTHING, db_column='wallet_payment', blank=True,
                                       null=True)
    amount = models.FloatField(blank=True, null=True)
    financial_year = models.ForeignKey(FinancialYear, models.DO_NOTHING, db_column='financial_year')
    is_trashed = models.IntegerField(blank=True, null=True)
    status = models.ForeignKey('SuspenseStatus', models.DO_NOTHING, db_column='status', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    received_on = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suspense_payment'


class SuspenseSettlement(models.Model):
    suspense_settlement_id = models.BigAutoField(primary_key=True)
    suspense_txn = models.ForeignKey(SuspensePayment, models.DO_NOTHING, db_column='suspense_txn', blank=True,
                                     null=True)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey('SuspenseStatus', models.DO_NOTHING, db_column='status', blank=True, null=True)
    initiated_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='initiated_by', blank=True, null=True)
    approved_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='approved_by', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suspense_settlement'


class SuspenseStatus(models.Model):
    suspense_status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suspense_status'


class UnitOfMeasure(models.Model):
    unit_of_measure_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    revenue_type = models.ForeignKey(RevenueType, models.DO_NOTHING, db_column='revenue_type')
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit_of_measure'


class UserStatus(models.Model):
    user_status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_status'


class UserType(models.Model):
    user_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_type'


class VehicleParking(models.Model):
    vehicle_parking_id = models.BigAutoField(primary_key=True)
    citizen = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='citizen', blank=True, null=True)
    parking_category = models.ForeignKey(RevenueCategory, models.DO_NOTHING, db_column='parking_category')
    parking_subcategory = models.ForeignKey(RevenueSubcategory, models.DO_NOTHING, db_column='parking_subcategory')
    validity_period = models.ForeignKey(UnitOfMeasure, models.DO_NOTHING, db_column='validity_period')
    buspark_matatu = models.ForeignKey(BusparkMatatu, models.DO_NOTHING, db_column='buspark_matatu', blank=True,
                                       null=True)
    sticker_number = models.CharField(max_length=250, blank=True, null=True)
    number_plate = models.CharField(max_length=250)
    valid_from = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)
    sub_county = models.ForeignKey(SubCounty, models.DO_NOTHING, db_column='sub_county', blank=True, null=True)
    ward = models.ForeignKey('Ward', models.DO_NOTHING, db_column='ward', blank=True, null=True)
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone', blank=True, null=True)
    initiated_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='initiated_by', blank=True, null=True)
    sticker_collected = models.IntegerField(blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_parking'


class WaiverConfig(models.Model):
    waiver_config_id = models.AutoField(primary_key=True)
    revenue_source = models.ForeignKey(RevenueSource, models.DO_NOTHING, db_column='revenue_source')
    financial_year = models.ForeignKey(FinancialYear, models.DO_NOTHING, db_column='financial_year')
    start_date = models.DateField()
    end_date = models.DateField()
    waiver_percent = models.FloatField()
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'waiver_config'


class WalletPayment(models.Model):
    wallet_payment_id = models.BigAutoField(primary_key=True)
    wallet_token = models.CharField(max_length=250)
    invoice = models.ForeignKey(InvoiceControl, models.DO_NOTHING, db_column='invoice')
    amount = models.FloatField()
    txn_code = models.CharField(max_length=250)
    wallet_holder = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='wallet_holder')
    financial_year = models.ForeignKey(FinancialYear, models.DO_NOTHING, db_column='financial_year')
    is_trashed = models.IntegerField(blank=True, null=True)
    received_on = models.DateTimeField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet_payment'


class Ward(models.Model):
    ward_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    sub_county = models.ForeignKey(SubCounty, models.DO_NOTHING, db_column='sub_county')
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ward'


class Zone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey(Operator, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zone'
