# Generated by Django 4.1 on 2023-03-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_b2b_product_investment_utr_detail_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b2b_product_investment_utr_detail',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='b2b_product_investment_utr_detail',
            name='txn_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]