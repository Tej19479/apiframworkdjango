# Generated by Django 4.1 on 2023-02-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_user_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='pin_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]