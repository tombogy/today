# Generated by Django 5.0.7 on 2024-09-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Driver', '0003_delete_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditpoint',
            name='status',
            field=models.CharField(choices=[('credited', 'Credited'), ('debited', 'Debited')], default='credited', max_length=20),
        ),
    ]
