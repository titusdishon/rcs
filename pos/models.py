from django.db import models
from django.conf import settings

from configurations.models import RevenueCategory, RevenueSubcategory, UnitOfMeasure, SubCounty, Zone, Ward
from organizations.models import Organization
from users.models import  Citizen


class SimCard(models.Model):
    sim_serial_number = models.CharField(max_length=250)
    sim_number = models.CharField(max_length=45)
    is_active = models.IntegerField(blank=True, null=True)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=False)
    updated_on = models.DateTimeField(auto_now_add=True)


class PosDevice(models.Model):
    description = models.CharField(max_length=250)
    imei = models.CharField(max_length=100)
    is_active = models.IntegerField(blank=True, null=True)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False, verbose_name="Active")
    created_on = models.DateTimeField(auto_now_add=False)
    updated_on = models.DateTimeField(auto_now_add=True)


class PosAssignment(models.Model):
    # operator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='operator')
    pos_device = models.ForeignKey(PosDevice, models.DO_NOTHING, db_column='pos_device')
    sim_card = models.ForeignKey(SimCard, models.DO_NOTHING, db_column='sim_card')
    assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='assigned_by')
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=False)
    updated_on = models.DateTimeField(auto_now_add=True)


class BusparkSacco(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=False)
    updated_on = models.DateTimeField(auto_now_add=True)


class BusparkMatatu(models.Model):
    citizen = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='citizen', blank=True, null=True)
    sacco = models.ForeignKey(BusparkSacco, models.DO_NOTHING, db_column='sacco', blank=True, null=True)
    registration_number = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=False)
    updated_on = models.DateTimeField(auto_now_add=True)


class VehicleParking(models.Model):
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
    ward = models.ForeignKey(Ward, models.DO_NOTHING, db_column='ward', blank=True, null=True)
    zone = models.ForeignKey(Zone, models.DO_NOTHING, db_column='zone', blank=True, null=True)
    initiated_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='initiated_by', blank=True,
                                     null=True)
    sticker_collected = models.IntegerField(blank=True, null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=False)
    updated_on = models.DateTimeField(auto_now_add=True)
