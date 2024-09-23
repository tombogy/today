# Generated by Django 5.0.7 on 2024-09-22 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0004_alter_trip_location'),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='fuel',
        ),
        migrations.AddField(
            model_name='trip',
            name='after_reach',
            field=models.ImageField(blank=True, null=True, upload_to='after_reach/'),
        ),
        migrations.AddField(
            model_name='trip',
            name='vehicle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='after_load_kg',
            field=models.ImageField(blank=True, null=True, upload_to='after_load_kg/'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='before_load_kg',
            field=models.ImageField(blank=True, null=True, upload_to='before_load_kg/'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='documents',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='location',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='meter_ra',
            field=models.ImageField(upload_to='meter_ra/'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='meter_rb',
            field=models.ImageField(upload_to='meter_rb/'),
        ),
    ]
