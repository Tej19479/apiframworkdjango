# Generated by Django 4.1 on 2023-03-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_b2b_product_investment_utr_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='b2b_product_investment_utr_detail',
            name='created',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]
