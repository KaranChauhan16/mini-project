# Generated by Django 4.2.11 on 2024-11-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_orderdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='user',
            field=models.CharField(default=True, max_length=15),
        ),
    ]