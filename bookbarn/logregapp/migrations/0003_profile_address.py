# Generated by Django 3.0.6 on 2020-09-09 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logregapp', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, default=''),
        ),
    ]
