# Generated by Django 3.1.2 on 2021-01-06 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0003_salesmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesmodel',
            name='bill_total',
            field=models.IntegerField(default=0),
        ),
    ]