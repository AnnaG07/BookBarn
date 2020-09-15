# Generated by Django 3.0.6 on 2020-09-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookbarnapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(),
        ),
    ]