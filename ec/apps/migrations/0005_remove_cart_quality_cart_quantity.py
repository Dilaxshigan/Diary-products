# Generated by Django 4.2.7 on 2024-01-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quality',
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
