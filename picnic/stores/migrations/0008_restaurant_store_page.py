# Generated by Django 4.0.1 on 2022-01-23 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_alter_restaurant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='store_page',
            field=models.URLField(default=''),
        ),
    ]
