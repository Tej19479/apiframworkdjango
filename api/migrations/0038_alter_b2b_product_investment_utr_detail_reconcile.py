# Generated by Django 4.1 on 2023-03-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_alter_b2b_product_investment_utr_detail_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b2b_product_investment_utr_detail',
            name='reconcile',
            field=models.CharField(default='N', max_length=3, null=True),
        ),
    ]
