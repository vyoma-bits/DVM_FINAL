# Generated by Django 5.0 on 2024-01-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0019_passengers_s1_passengers_s2'),
    ]

    operations = [
        migrations.AddField(
            model_name='journeys',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
