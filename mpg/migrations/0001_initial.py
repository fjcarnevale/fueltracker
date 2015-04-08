# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('gallons', models.FloatField()),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('make', models.ForeignKey(to='mpg.Make')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('model', models.ForeignKey(to='mpg.Model')),
            ],
        ),
        migrations.AddField(
            model_name='fuelup',
            name='vehicle',
            field=models.ForeignKey(to='mpg.Vehicle'),
        ),
    ]
