# Generated by Django 3.1.2 on 2020-10-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tissue_collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='last_updated',
            field=models.DateField(),
        ),
    ]
