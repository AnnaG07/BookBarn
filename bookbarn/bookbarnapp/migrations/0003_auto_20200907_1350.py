# Generated by Django 3.0.6 on 2020-09-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logregapp', '0001_initial'),
        ('bookbarnapp', '0002_auto_20200905_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='faves',
            field=models.ManyToManyField(blank=True, related_name='faved_books', to='logregapp.User'),
        ),
    ]