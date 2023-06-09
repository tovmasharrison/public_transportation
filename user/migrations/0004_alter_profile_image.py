# Generated by Django 4.1.6 on 2023-02-22 15:09

from django.db import migrations, models

import helpers.image_paths


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0003_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="static/user/image/default_profile.jpg",
                upload_to=helpers.image_paths.upload_profile_image,
            ),
        ),
    ]
