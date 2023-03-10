# Generated by Django 4.1 on 2023-02-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_user_verification'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=75, null=True)),
                ('deleted', models.CharField(max_length=5)),
                ('dob', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('PAN', models.CharField(blank=True, max_length=100, null=True)),
                ('aadhaar_number', models.CharField(blank=True, max_length=14, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
