# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-02 18:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deaspo', '0021_auto_20170102_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productweborder',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 2, 21, 6, 35, 131000), editable=False),
        ),
        migrations.AlterField(
            model_name='usernext',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 2, 21, 6, 35, 131000)),
        ),
    ]
