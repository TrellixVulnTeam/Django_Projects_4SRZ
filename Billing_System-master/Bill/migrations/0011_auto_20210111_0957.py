# Generated by Django 3.1.2 on 2021-01-11 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0010_auto_20210111_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='bill_number',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='product_name',
            field=models.CharField(max_length=120),
        ),
    ]
