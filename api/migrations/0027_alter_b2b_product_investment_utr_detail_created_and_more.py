# Generated by Django 4.1 on 2023-03-04 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_b2b_product_investment_utr_detail_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b2b_product_investment_utr_detail',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 4, 23, 44, 18, 849987), null=True),
        ),
        migrations.AlterField(
            model_name='b2b_product_investment_utr_detail',
            name='txn_date',
            field=models.DateTimeField(),
        ),
    ]