# Generated by Django 2.1.1 on 2018-09-22 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20180922_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='quiz',
            name='negative',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='quiz',
            name='positive',
            field=models.IntegerField(default=3),
        ),
    ]