# Generated by Django 4.1.6 on 2023-02-16 08:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0004_alter_review_name_alter_review_rate_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Minimum value must be 0.'), django.core.validators.MaxValueValidator(5, message='Maximum value must be 5.')]),
        ),
    ]
