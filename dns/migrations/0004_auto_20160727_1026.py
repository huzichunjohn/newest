# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dns', '0003_auto_20160727_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a',
            name='ttl',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
