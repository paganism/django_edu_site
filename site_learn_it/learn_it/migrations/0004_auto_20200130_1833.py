# Generated by Django 3.0.2 on 2020-01-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_it', '0003_course_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='timetable',
        ),
        migrations.AddField(
            model_name='course',
            name='day',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
    ]
