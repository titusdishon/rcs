# Generated by Django 2.2 on 2019-05-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0002_auto_20190501_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenuecategory',
            name='pos_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='revenuesource',
            name='pos_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='revenuesubcategory',
            name='pos_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='revenuetype',
            name='pos_enabled',
            field=models.BooleanField(default=False),
        ),
    ]