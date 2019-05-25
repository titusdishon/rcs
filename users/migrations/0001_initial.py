# Generated by Django 2.2 on 2019-05-01 08:19

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
        ('configurations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_trashed', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoleCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('is_active', models.IntegerField(default=0)),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(db_column='organization', on_delete=django.db.models.deletion.DO_NOTHING, to='organizations.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IdType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CountyAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('registration_number', models.CharField(max_length=250)),
                ('kra_pin_number', models.CharField(max_length=250)),
                ('physical_address', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=250)),
                ('postal_address', models.CharField(max_length=250)),
                ('apply_flat_commission', models.IntegerField(blank=True, null=True)),
                ('commission', models.FloatField(blank=True, null=True)),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('sub_county', models.ForeignKey(db_column='sub_county', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.SubCounty')),
                ('ward', models.ForeignKey(db_column='ward', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.Ward')),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('id_number', models.CharField(blank=True, max_length=250, null=True)),
                ('kra_pin', models.CharField(blank=True, max_length=50, null=True)),
                ('is_county_resident', models.IntegerField(blank=True, null=True)),
                ('allow_system_access', models.IntegerField(blank=True, null=True)),
                ('create_wallet_account', models.IntegerField(blank=True, null=True)),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('county', models.ForeignKey(blank=True, db_column='county', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.County')),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('id_type', models.ForeignKey(db_column='id_type', on_delete=django.db.models.deletion.DO_NOTHING, to='users.IdType')),
                ('nationality', models.ForeignKey(db_column='nationality', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.Country')),
                ('sub_county', models.ForeignKey(blank=True, db_column='sub_county', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.SubCounty')),
                ('ward', models.ForeignKey(blank=True, db_column='ward', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.Ward')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='agent',
            field=models.ForeignKey(blank=True, db_column='agent', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.CountyAgent'),
        ),
        migrations.AddField(
            model_name='user',
            name='citizen_st',
            field=models.ForeignKey(blank=True, db_column='citizen', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Citizen'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(blank=True, db_column='organization', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='user',
            name='role_center',
            field=models.ForeignKey(blank=True, db_column='role_center', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.RoleCenter'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_status',
            field=models.ForeignKey(blank=True, db_column='user_status', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserStatus'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserType'),
        ),
    ]