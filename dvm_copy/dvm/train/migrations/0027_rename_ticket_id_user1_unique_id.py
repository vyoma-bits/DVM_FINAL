# Generated by Django 5.0 on 2024-01-05 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0026_journeys_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user1',
            old_name='ticket_id',
            new_name='unique_id',
        ),
    ]
