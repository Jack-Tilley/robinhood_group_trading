# Generated by Django 3.1.6 on 2021-03-07 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_investment_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='api.instrument'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='api.portfolio'),
        ),
    ]
