# Generated by Django 4.0.1 on 2022-01-23 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(upload_to='uploads/<django.db.models.fields.CharField>'),
        ),
    ]
