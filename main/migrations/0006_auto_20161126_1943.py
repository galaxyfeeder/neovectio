# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20161126_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buses', to='main.Line'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='latitude',
            field=models.DecimalField(decimal_places=8, max_digits=10),
        ),
        migrations.AlterField(
            model_name='station',
            name='longitude',
            field=models.DecimalField(decimal_places=8, max_digits=10),
        ),
    ]