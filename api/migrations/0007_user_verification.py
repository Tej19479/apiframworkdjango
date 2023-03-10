# Generated by Django 4.1 on 2023-02-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_cnd_cnd_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(blank=True, null=True)),
                ('verification_type', models.CharField(blank=True, max_length=100, null=True)),
                ('deleted', models.CharField(max_length=5)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
