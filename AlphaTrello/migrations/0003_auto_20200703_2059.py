# Generated by Django 3.0.8 on 2020-07-03 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlphaTrello', '0002_auto_20200702_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='memebers',
            new_name='members',
        ),
    ]
