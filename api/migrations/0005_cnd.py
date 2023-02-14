# Generated by Django 4.1 on 2023-02-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_bank_details_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='cnd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnd_name', models.CharField(max_length=200)),
                ('cnd_code', models.CharField(max_length=256)),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('deleted', models.CharField(max_length=5)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('cnd_parent_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
