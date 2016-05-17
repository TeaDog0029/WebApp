# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_tint_number_of_clicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='tint',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tint',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tint',
            name='image',
            field=models.ImageField(blank=True, height_field=b'height_field', null=True, upload_to=b'', width_field=b'width_field'),
        ),
    ]