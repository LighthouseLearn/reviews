# Generated by Django 2.2.6 on 2019-10-27 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20191027_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='unit_address',
            new_name='address',
        ),
    ]
