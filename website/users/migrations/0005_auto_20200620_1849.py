# Generated by Django 3.0.7 on 2020-06-20 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200620_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medication',
            old_name='sideeffects',
            new_name='side_effects',
        ),
        migrations.RenameField(
            model_name='medication',
            old_name='treatmentFor',
            new_name='treatment_for',
        ),
    ]
