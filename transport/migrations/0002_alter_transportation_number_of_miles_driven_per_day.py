# Generated by Django 4.1.6 on 2023-02-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportation',
            name='number_of_miles_driven_per_day',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]