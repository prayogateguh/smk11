# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-01 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0004_auto_20180101_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='embed',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
