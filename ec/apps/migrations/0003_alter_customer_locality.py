# Generated by Django 4.2.7 on 2024-01-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='locality',
            field=models.CharField(max_length=255),
        ),
    ]
