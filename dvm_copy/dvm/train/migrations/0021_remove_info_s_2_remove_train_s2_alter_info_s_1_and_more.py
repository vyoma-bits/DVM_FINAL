# Generated by Django 5.0 on 2024-01-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0020_journeys_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='s_2',
        ),
        migrations.RemoveField(
            model_name='train',
            name='s2',
        ),
        migrations.AlterField(
            model_name='info',
            name='s_1',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='train',
            name='s1',
            field=models.CharField(max_length=250),
        ),
    ]
