# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='code',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
