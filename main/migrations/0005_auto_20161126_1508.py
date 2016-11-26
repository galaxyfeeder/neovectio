# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20161126_1124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stop',
            options={'ordering': ('order',)},
        ),
        migrations.AlterField(
            model_name='stop',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stops', to='main.Line'),
        ),
    ]
