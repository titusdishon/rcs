# Generated by Django 2.2 on 2019-05-01 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('configurations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ward',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ward',
            name='sub_county',
            field=models.ForeignKey(db_column='sub_county', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.SubCounty'),
        ),
        migrations.AddField(
            model_name='unitofmeasure',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='unitofmeasure',
            name='revenue_type',
            field=models.ForeignKey(db_column='revenue_type', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.RevenueType'),
        ),
        migrations.AddField(
            model_name='subcounty',
            name='county',
            field=models.ForeignKey(db_column='county', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.County'),
        ),
        migrations.AddField(
            model_name='subcounty',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='revenuetype',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='revenuetype',
            name='revenue_source',
            field=models.ForeignKey(db_column='revenue_source', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.RevenueSource'),
        ),
        migrations.AddField(
            model_name='revenuesubcategory',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='revenuesubcategory',
            name='revenue_category',
            field=models.ForeignKey(db_column='revenue_category', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.RevenueCategory'),
        ),
        migrations.AddField(
            model_name='revenuesource',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='revenuesource',
            name='general_ledger',
            field=models.ForeignKey(blank=True, db_column='general_ledger', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.ChartOfAccount'),
        ),
        migrations.AddField(
            model_name='revenuecostmatrix',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='revenuecostmatrix',
            name='financial_year',
            field=models.ForeignKey(db_column='financial_year', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.FinancialYear'),
        ),
        migrations.AddField(
            model_name='revenuecostmatrix',
            name='revenue_category',
            field=models.ForeignKey(db_column='revenue_category', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.RevenueCategory'),
        ),
        migrations.AddField(
            model_name='revenuecostmatrix',
            name='revenue_source',
            field=models.ForeignKey(db_column='revenue_source', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.RevenueSource'),
        ),
        migrations.AddField(
            model_name='revenuecostmatrix',
            name='revenue_subcategory',
            field=models.ForeignKey(db_column='revenue_subcategory', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.RevenueSubcategory'),
        ),
        migrations.AddField(
            model_name='revenuecostmatrix',
            name='revenue_type',
            field=models.ForeignKey(db_column='revenue_type', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.RevenueType'),
        ),
        migrations.AddField(
            model_name='revenuecostmatrix',
            name='unit_of_measure',
            field=models.ForeignKey(blank=True, db_column='unit_of_measure', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.UnitOfMeasure'),
        ),
        migrations.AddField(
            model_name='revenuecategory',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='revenuecategory',
            name='revenue_type',
            field=models.ForeignKey(db_column='revenue_type', on_delete=django.db.models.deletion.DO_NOTHING, to='configurations.RevenueType'),
        ),
        migrations.AddField(
            model_name='paymentchannel',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='financialyear',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='county',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='country',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chartofaccount',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]