# Generated by Django 3.0.5 on 2020-04-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0007_auto_20200424_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='picture',
            field=models.ImageField(blank=True, upload_to='menu_image'),
        ),
    ]
