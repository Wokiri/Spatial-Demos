# Generated by Django 3.1.4 on 2021-02-23 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spatialdemos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
