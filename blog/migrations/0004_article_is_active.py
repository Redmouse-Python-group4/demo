# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161024_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
