# Generated by Django 4.1 on 2023-03-05 15:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_alter_b2b_product_investment_utr_detail_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b2b_product_investment_utr_detail',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
