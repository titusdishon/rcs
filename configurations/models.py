from django.db import models
from django.conf import settings


class County(models.Model):
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True,  auto_now_add=True, null=True)
    updated_on = models.DateTimeField(blank=True, auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class SubCounty(models.Model):
    name = models.CharField(max_length=250)
    county = models.ForeignKey(County, models.DO_NOTHING, db_column='county')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Ward(models.Model):
    name = models.CharField(max_length=250)
    sub_county = models.ForeignKey(SubCounty, models.DO_NOTHING, db_column='sub_county')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Zone(models.Model):
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class FinancialYear(models.Model):
    name = models.CharField(max_length=250)
    start_on = models.DateTimeField()
    end_on = models.DateTimeField()
    is_current = models.IntegerField(blank=True, null=True)
    is_trashed = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class ChartOfAccount(models.Model):
    gl_code = models.CharField(max_length=250)
    gl_name = models.CharField(max_length=250)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField( auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RevenueSource(models.Model):
    name = models.CharField(max_length=250)
    pos_enabled = models.BooleanField(default=False)
    general_ledger = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, db_column='general_ledger', blank=True,
                                       null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=False)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RevenueType(models.Model):
    revenue_source = models.ForeignKey(RevenueSource, models.DO_NOTHING, db_column='revenue_source')
    name = models.CharField(max_length=250)
    pos_enabled = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=False)
    updated_on = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name


class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=250)
    revenue_type = models.ForeignKey(RevenueType, models.DO_NOTHING, db_column='revenue_type')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class RevenueCategory(models.Model):
    name = models.CharField(max_length=250)
    revenue_type = models.ForeignKey(RevenueType, models.DO_NOTHING, db_column='revenue_type')
    pos_enabled = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class RevenueSubcategory(models.Model):
    revenue_category = models.ForeignKey(RevenueCategory, models.DO_NOTHING, db_column='revenue_category')
    name = models.CharField(max_length=250)
    pos_enabled = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class RevenueCostMatrix(models.Model):
    financial_year = models.ForeignKey(FinancialYear, models.DO_NOTHING, db_column='financial_year')
    revenue_source = models.ForeignKey(RevenueSource, models.DO_NOTHING, db_column='revenue_source')
    revenue_type = models.ForeignKey(RevenueType, models.DO_NOTHING, db_column='revenue_type')
    revenue_category = models.ForeignKey(RevenueCategory, models.DO_NOTHING, db_column='revenue_category')
    revenue_subcategory = models.ForeignKey(RevenueSubcategory, models.DO_NOTHING, db_column='revenue_subcategory')
    unit_of_measure = models.ForeignKey(UnitOfMeasure, models.DO_NOTHING, db_column='unit_of_measure', blank=True,
                                        null=True)
    cost = models.FloatField()
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    is_current = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class PaymentChannel(models.Model):
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
