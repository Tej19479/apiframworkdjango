# Generated by Django 4.1 on 2023-03-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_b2b_product_investment_utr_detail_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b2b_product_investment_utr_detail',
            name='txn_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]