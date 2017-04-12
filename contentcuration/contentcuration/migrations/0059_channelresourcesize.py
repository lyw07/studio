# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-10 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0058_auto_20170223_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelResourceSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree_id', models.IntegerField()),
                ('resource_size', models.IntegerField()),
            ],
            options={
                'db_table': 'contentcuration_channel_resource_sizes',
                'managed': False,
            },
        ),
    ]