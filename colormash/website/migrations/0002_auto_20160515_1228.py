# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tint',
            name='elo',
            field=models.IntegerField(default=1400),
        ),
        migrations.AddField(
            model_name='tint',
            name='rank',
            field=models.IntegerField(default=999),
        ),
        migrations.AlterField(
            model_name='tint',
            name='hex_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tint',
            name='rgb_name',
            field=models.CharField(max_length=30),
        ),
    ]
