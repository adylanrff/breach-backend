# Generated by Django 2.2 on 2019-04-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0007_auto_20190428_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
