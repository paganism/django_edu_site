# Generated by Django 3.0.2 on 2020-01-30 16:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learn_it', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_start',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
