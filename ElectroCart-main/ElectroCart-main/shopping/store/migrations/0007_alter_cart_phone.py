# Generated by Django 4.2.11 on 2024-11-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
