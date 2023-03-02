# Generated by Django 4.1 on 2023-02-28 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_cnd_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='b2b_product_investment_utr_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(blank=True, null=True)),
                ('investment_id', models.BigIntegerField(blank=True, null=True)),
                ('plan_id', models.BigIntegerField(blank=True, null=True)),
                ('pool_id', models.BigIntegerField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('schema_id', models.CharField(blank=True, max_length=256, null=True)),
                ('utr_no', models.CharField(blank=True, max_length=256, null=True)),
                ('txn_id', models.BigIntegerField(blank=True, null=True)),
                ('reconcile', models.CharField(blank=True, max_length=2, null=True)),
                ('escrow_status', models.CharField(blank=True, max_length=2, null=True)),
                ('deleted', models.CharField(blank=True, max_length=2, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=225, null=True)),
                ('callback_url', models.CharField(blank=True, max_length=225, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('txn_status', models.IntegerField(blank=True, null=True)),
                ('txn_date', models.DateTimeField(blank=True, null=True)),
                ('bank_ref_id', models.CharField(blank=True, max_length=225, null=True)),
                ('utr_post_date', models.DateTimeField(blank=True, null=True)),
                ('utr_share_date', models.DateField(auto_now_add=True)),
                ('is_funding_started', models.CharField(blank=True, max_length=2, null=True)),
                ('pg_type', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_mode', models.CharField(blank=True, max_length=50, null=True)),
                ('recharge_ref_id', models.IntegerField(blank=True, null=True)),
                ('pool_loan_id', models.BigIntegerField(blank=True, null=True)),
                ('proposal_id', models.IntegerField(blank=True, null=True)),
                ('actual_utr_amount_credit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='inv',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
