# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-13 02:17
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0104_auto_20191028_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='published_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]