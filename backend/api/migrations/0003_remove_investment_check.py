# Generated by Django 3.1.6 on 2021-03-07 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210307_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investment',
            name='check',
        ),
    ]
