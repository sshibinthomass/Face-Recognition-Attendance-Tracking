# Generated by Django 2.2.5 on 2022-04-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
