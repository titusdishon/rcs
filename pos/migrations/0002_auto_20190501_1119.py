# Generated by Django 2.2 on 2019-05-01 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0002_auto_20190501_1119'),
        ('pos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simcard',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='simcard',
            name='organization',
            field=models.ForeignKey(db_column='organization', on_delete=django.db.models.deletion.DO_NOTHING, to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='posdevice',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posdevice',
            name='organization',
            field=models.ForeignKey(db_column='organization', on_delete=django.db.models.deletion.DO_NOTHING, to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='posassignment',
            name='assigned_by',
            field=models.ForeignKey(db_column='assigned_by', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posassignment',
            name='pos_device',
            field=models.ForeignKey(db_column='pos_device', on_delete=django.db.models.deletion.DO_NOTHING, to='pos.PosDevice'),
        ),
        migrations.AddField(
            model_name='posassignment',
            name='sim_card',
            field=models.ForeignKey(db_column='sim_card', on_delete=django.db.models.deletion.DO_NOTHING, to='pos.SimCard'),
        ),
    ]