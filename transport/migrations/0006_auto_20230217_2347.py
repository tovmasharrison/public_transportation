# Generated by Django 3.2.5 on 2023-02-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # ('stop', '0001_initial'),
        ('transport', '0005_alter_review_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transportation',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='transportation',
            name='number_of_miles_driven_per_day',
        ),
        migrations.AddField(
            model_name='transportation',
            name='stop',
            field=models.ManyToManyField(related_name='transports', to='stop.BusStop'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='type',
            field=models.CharField(choices=[('bus', 'Bus'), ('microbus', 'Microbus'), ('trolleybus', 'Trolleybus'), ('metro', 'Metro')], max_length=30),
        ),
    ]
