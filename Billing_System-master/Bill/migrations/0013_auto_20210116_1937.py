# Generated by Django 3.1.2 on 2021-01-16 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0012_ordermodel_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
