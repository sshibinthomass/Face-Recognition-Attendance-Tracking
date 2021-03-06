# Generated by Django 2.2.5 on 2022-04-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20220410_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='description',
            field=models.TextField(blank=True, default='def'),
        ),
        migrations.AddField(
            model_name='destination',
            name='img',
            field=models.ImageField(default='pics/default.png', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='destination',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='name',
            field=models.CharField(default='def', max_length=100),
        ),
        migrations.AddField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
