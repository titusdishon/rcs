from django.conf import settings
from django.db import models
from configurations.models import County, SubCounty, Ward


class OrganizationCategory(models.Model):
    name = models.CharField(max_length=250)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)


class Organization(models.Model):
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    category = models.ForeignKey(OrganizationCategory, models.DO_NOTHING, db_column='category')
    organization_parent = models.IntegerField()
    county = models.ForeignKey(County, models.DO_NOTHING, db_column='county', blank=True, null=True)
    sub_county = models.ForeignKey(SubCounty, models.DO_NOTHING, db_column='sub_county', blank=True, null=True)
    ward = models.ForeignKey(Ward, models.DO_NOTHING, db_column='ward', blank=True, null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    update_on = models.DateTimeField(blank=True, null=True)


class Resource(models.Model):
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=45)
    icon = models.CharField(max_length=45)
    enabled = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)


class ResourceAction(models.Model):
    resource = models.ForeignKey(Resource, models.DO_NOTHING, db_column='resource')
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=45)
    icon = models.CharField(max_length=45)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)


class OrganizationAction(models.Model):
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization')
    action = models.ForeignKey(ResourceAction, models.DO_NOTHING, db_column='action')
    resource = models.ForeignKey(Resource, models.DO_NOTHING, db_column='resource')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    update_on = models.DateTimeField(blank=True, null=True)
