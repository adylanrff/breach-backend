# Generated by Django 2.2 on 2019-04-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0013_auto_20190428_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='place_status',
        ),
        migrations.AddField(
            model_name='journey',
            name='place',
            field=models.ManyToManyField(to='journey.Place'),
        ),
        migrations.DeleteModel(
            name='PlaceJourneyStatus',
        ),
    ]
