# Generated by Django 4.2.16 on 2024-12-10 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='status',
            field=models.IntegerField(choices=[(1, 'فعال'), (2, 'غیرفعال')], default=2),
        ),
    ]
