# Generated by Django 4.1 on 2023-02-14 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_user_details_pin_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='dob',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
