# Generated by Django 3.1.6 on 2021-02-20 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_post_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='score', to='api.score'),
            preserve_default=False,
        ),
    ]
