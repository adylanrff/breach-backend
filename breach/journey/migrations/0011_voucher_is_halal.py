# Generated by Django 2.2 on 2019-04-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0010_auto_20190428_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='is_halal',
            field=models.BooleanField(default=True),
        ),
    ]
