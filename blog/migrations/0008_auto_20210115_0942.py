# Generated by Django 3.1.5 on 2021-01-15 09:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210114_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 9, 42, 17, 990104, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 9, 42, 17, 988282, tzinfo=utc)),
        ),
    ]