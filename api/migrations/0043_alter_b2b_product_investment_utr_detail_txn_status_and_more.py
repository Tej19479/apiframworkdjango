# Generated by Django 4.1 on 2023-03-07 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_alter_b2b_product_investment_utr_detail_escrow_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b2b_product_investment_utr_detail',
            name='txn_status',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='b2b_product_investment_utr_detail',
            name='updated_by',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
