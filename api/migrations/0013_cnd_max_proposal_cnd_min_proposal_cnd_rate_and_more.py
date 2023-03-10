# Generated by Django 4.1 on 2023-02-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_docstore'),
    ]

    operations = [
        migrations.AddField(
            model_name='cnd',
            name='max_proposal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cnd',
            name='min_proposal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cnd',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='docstore',
            name='pimage',
            field=models.ImageField(blank=True, null=True, upload_to='pimages'),
        ),
    ]
