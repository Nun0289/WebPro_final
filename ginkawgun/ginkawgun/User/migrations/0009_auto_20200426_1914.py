# Generated by Django 3.0.5 on 2020-04-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_auto_20200426_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user_picture',
        ),
        migrations.AddField(
            model_name='customer',
            name='userpicture',
            field=models.ImageField(blank=True, upload_to='user_image'),
        ),
    ]