# Generated by Django 3.1.2 on 2020-11-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institution', '0002_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='experience',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='hourlyRate',
            field=models.IntegerField(),
        ),
    ]