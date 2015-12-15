# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('name_slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('casenumber', models.CharField(max_length=10)),
                ('reported', models.DateField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('stolen', models.FloatField()),
                ('damaged', models.FloatField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Incidentcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('name_slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('name_slug', models.SlugField()),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('building', models.ForeignKey(blank=True, to='crimemap.Building', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('name_slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='incident',
            name='incidentcode',
            field=models.ForeignKey(to='crimemap.Incidentcode'),
        ),
        migrations.AddField(
            model_name='incident',
            name='location',
            field=models.ForeignKey(to='crimemap.Location'),
        ),
        migrations.AddField(
            model_name='incident',
            name='status',
            field=models.ForeignKey(to='crimemap.Status'),
        ),
    ]
