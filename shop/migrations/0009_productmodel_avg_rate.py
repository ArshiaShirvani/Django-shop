# Generated by Django 4.2.16 on 2025-01-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_wishlistmodel_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='avg_rate',
            field=models.FloatField(default=0.0),
        ),
    ]
