# Generated by Django 4.0.1 on 2022-01-28 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'ordering': ('start_time',)},
        ),
    ]
