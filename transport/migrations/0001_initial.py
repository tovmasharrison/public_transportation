# Generated by Django 4.1.6 on 2023-02-08 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('type', models.CharField(choices=[('bus', 'Bus'), ('microbus', 'Microbus'), ('trolleybus', 'Trolleybus')], max_length=30)),
                ('route', models.TextField()),
                ('number_of_miles_driven_per_day', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.AddIndex(
            model_name='transportation',
            index=models.Index(fields=['-number'], name='transport_t_number_f05808_idx'),
        ),
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='transport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='transport.transportation'),
        ),
        migrations.AddField(
            model_name='busstop',
            name='transport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stops', to='transport.transportation'),
        ),
    ]