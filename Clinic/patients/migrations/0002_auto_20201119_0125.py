# Generated by Django 3.1.2 on 2020-11-18 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='user',
            field=models.CharField(max_length=120),
        ),
    ]
