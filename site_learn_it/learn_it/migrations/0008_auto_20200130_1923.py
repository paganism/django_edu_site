# Generated by Django 3.0.2 on 2020-01-30 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_it', '0007_auto_20200130_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='day',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='день недели'),
        ),
    ]
