# Generated by Django 2.2 on 2020-07-04 21:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200703_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='queriedAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 2, 16, 5, 887967, tzinfo=utc)),
        ),
    ]
