# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-27 11:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deaspo', '0013_auto_20161224_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField(max_length=3000)),
                ('posted', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='deaspo.Product')),
            ],
        ),
        migrations.AlterField(
            model_name='productweborder',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 27, 14, 54, 47, 882000), editable=False),
        ),
        migrations.AlterField(
            model_name='usernext',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 27, 14, 54, 47, 883000)),
        ),
    ]
