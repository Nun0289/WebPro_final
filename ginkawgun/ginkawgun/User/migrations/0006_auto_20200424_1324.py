# Generated by Django 3.0.5 on 2020-04-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_auto_20200424_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_picture',
            field=models.ImageField(blank=True, null=True, upload_to='user_image'),
        ),
    ]
