# Generated by Django 2.0 on 2018-01-23 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20180123_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
