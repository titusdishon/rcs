# Generated by Django 2.2 on 2019-05-03 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20190501_1119'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_trashed', models.BooleanField(default=False, verbose_name='active')),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('resource', models.ForeignKey(db_column='resource', on_delete=django.db.models.deletion.DO_NOTHING, to='organizations.Resource')),
                ('role_action', models.ForeignKey(db_column='role_action', on_delete=django.db.models.deletion.DO_NOTHING, to='organizations.ResourceAction')),
                ('role_center', models.ForeignKey(db_column='role_center', on_delete=django.db.models.deletion.DO_NOTHING, to='users.RoleCenter')),
            ],
        ),
    ]