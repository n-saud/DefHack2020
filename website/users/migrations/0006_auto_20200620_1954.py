# Generated by Django 3.0.7 on 2020-06-20 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200620_1849'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Log',
            new_name='SymptomLog',
        ),
        migrations.AddField(
            model_name='medication',
            name='dosage',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='MedLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('number_of_doses', models.FloatField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Customer')),
                ('medication', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Medication')),
            ],
        ),
    ]
