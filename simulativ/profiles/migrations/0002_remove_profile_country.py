# Generated by Django 3.0.5 on 2020-04-27 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
    ]
