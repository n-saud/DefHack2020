# Generated by Django 3.0.7 on 2020-06-21 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200620_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='symptomlog',
            old_name='durarion_in_hours',
            new_name='duration_in_hours',
        ),
    ]
