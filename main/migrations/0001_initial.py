# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_capacity', models.PositiveIntegerField()),
                ('latitude', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('load', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=10)),
                ('people_waiting', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Line')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Station')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='station',
            unique_together=set([('latitude', 'longitude')]),
        ),
        migrations.AddField(
            model_name='bus',
            name='last_stop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Stop'),
        ),
        migrations.AddField(
            model_name='bus',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Line'),
        ),
        migrations.AlterUniqueTogether(
            name='stop',
            unique_together=set([('line', 'order'), ('line', 'station')]),
        ),
    ]
