# Generated by Django 2.2.5 on 2022-04-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackingDetails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackers',
            name='empId',
            field=models.CharField(default='EMP0001', max_length=100),
        ),
    ]
