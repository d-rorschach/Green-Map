# Generated by Django 3.1.1 on 2021-03-20 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountholder',
            name='carbon_footprint',
            field=models.FloatField(default=0),
        ),
    ]
