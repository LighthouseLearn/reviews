# Generated by Django 2.2.6 on 2019-11-25 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_auto_20191124_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='maintenance_quality',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='move_in_condition',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='response_speed',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='treatment',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
        ),
    ]
