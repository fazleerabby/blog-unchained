# Generated by Django 2.0 on 2018-01-23 15:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20180123_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 23, 15, 39, 16, 981592, tzinfo=utc)),
        ),
    ]
