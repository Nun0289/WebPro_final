# Generated by Django 3.0.5 on 2020-04-24 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20200423_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user_picture',
            field=models.ImageField(blank=True, upload_to='static/image/user_image'),
        ),
    ]