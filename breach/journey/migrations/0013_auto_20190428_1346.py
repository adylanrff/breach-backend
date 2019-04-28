# Generated by Django 2.2 on 2019-04-28 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0012_auto_20190428_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='place',
        ),
        migrations.CreateModel(
            name='PlaceJourneyStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_visited', models.BooleanField(default=False)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journey.Place')),
            ],
        ),
        migrations.AddField(
            model_name='journey',
            name='place_status',
            field=models.ManyToManyField(to='journey.PlaceJourneyStatus'),
        ),
    ]