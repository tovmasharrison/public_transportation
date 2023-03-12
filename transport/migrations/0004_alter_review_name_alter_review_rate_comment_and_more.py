# Generated by Django 4.1.6 on 2023-02-16 08:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transport', '0003_alter_review_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='transport.review')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['created'], name='transport_c_created_ae6ba9_idx'),
        ),
    ]
