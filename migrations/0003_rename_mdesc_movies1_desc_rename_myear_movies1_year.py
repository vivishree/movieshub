# Generated by Django 4.2.7 on 2024-02-07 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_movies1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies1',
            old_name='mdesc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='movies1',
            old_name='myear',
            new_name='year',
        ),
    ]