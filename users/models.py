from PIL import Image
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from configurations.models import Country, County, SubCounty, Ward
from organizations.models import Organization, ResourceAction, Resource


class UserType(models.Model):
    name = models.CharField(max_length=250)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class UserStatus(models.Model):
    name = models.CharField(max_length=250)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class CountyAgent(models.Model):
    name = models.CharField(max_length=250)
    registration_number = models.CharField(max_length=250)
    kra_pin_number = models.CharField(max_length=250)
    sub_county = models.ForeignKey(SubCounty, models.DO_NOTHING, db_column='sub_county')
    ward = models.ForeignKey(Ward, models.DO_NOTHING, db_column='ward')
    physical_address = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    postal_address = models.CharField(max_length=250)
    apply_flat_commission = models.IntegerField(blank=True, null=True)
    commission = models.FloatField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class IdType(models.Model):
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True,
                                   null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Citizen(models.Model):
    name = models.CharField(max_length=250)
    id_type = models.ForeignKey(IdType, models.DO_NOTHING, db_column='id_type')
    id_number = models.CharField(max_length=250, blank=True, null=True)
    kra_pin = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.ForeignKey(Country, models.DO_NOTHING, db_column='nationality')
    is_county_resident = models.IntegerField(blank=True, null=True)
    county = models.ForeignKey(County, models.DO_NOTHING, db_column='county', blank=True, null=True)
    sub_county = models.ForeignKey(SubCounty, models.DO_NOTHING, db_column='sub_county', blank=True, null=True)
    ward = models.ForeignKey(Ward, models.DO_NOTHING, db_column='ward', blank=True, null=True)
    allow_system_access = models.IntegerField(blank=True, null=True)
    create_wallet_account = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class RoleCenter(models.Model):
    name = models.CharField(max_length=250)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization')
    is_active = models.IntegerField(default=0)
    is_trashed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=False)
    updated_on = models.DateTimeField(auto_now_add=True)


class User(AbstractUser):
    mobile = models.CharField(max_length=250)
    user_type = models.ForeignKey(UserType, models.DO_NOTHING, blank=True, null=True)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization', blank=True, null=True)
    role_center = models.ForeignKey(RoleCenter, models.DO_NOTHING, db_column='role_center', blank=True, null=True)
    agent = models.ForeignKey(CountyAgent, models.DO_NOTHING, db_column='agent', blank=True, null=True)
    citizen_st = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='citizen', blank=True, null=True)
    user_status = models.ForeignKey(UserStatus, models.DO_NOTHING, db_column='user_status', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_trashed = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class RoleAction(models.Model):
    role_center = models.ForeignKey(RoleCenter, models.DO_NOTHING, db_column='role_center')
    role_action = models.ForeignKey(ResourceAction, models.DO_NOTHING, db_column='role_action')
    resource = models.ForeignKey(Resource, models.DO_NOTHING, db_column='resource')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_trashed = models.BooleanField(default=False, verbose_name='active')
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.role_center


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField( max_length=13, blank=False, null=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)
