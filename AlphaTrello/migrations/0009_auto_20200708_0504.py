# Generated by Django 3.0.8 on 2020-07-08 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlphaTrello', '0008_auto_20200706_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='src',
            field=models.FileField(upload_to='uploads'),
        ),
    ]
