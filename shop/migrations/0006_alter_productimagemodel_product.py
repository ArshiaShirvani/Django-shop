# Generated by Django 4.2.16 on 2024-12-16 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_productmodel_discount_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimagemodel',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='shop.productmodel'),
        ),
    ]
