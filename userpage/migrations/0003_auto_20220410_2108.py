# Generated by Django 2.2.5 on 2022-04-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0002_userdetails_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='empDOB',
            field=models.DateTimeField(blank=True),
        ),
    ]
