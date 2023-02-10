# Generated by Django 4.1 on 2023-02-08 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_state', models.IntegerField(default=0)),
                ('deleted', models.CharField(max_length=5)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
