# Generated by Django 4.1.6 on 2023-02-12 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transport', '0002_alter_transportation_number_of_miles_driven_per_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='review', to=settings.AUTH_USER_MODEL),
        ),
    ]
