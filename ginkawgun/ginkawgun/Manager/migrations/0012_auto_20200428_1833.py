# Generated by Django 3.0.5 on 2020-04-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0011_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('เสร็จแล้ว', 'success'), ('กำลังทำ', 'inprogress'), ('ยกเลิก', 'cancel')], default='กำลังทำ', max_length=15),
        ),
    ]
