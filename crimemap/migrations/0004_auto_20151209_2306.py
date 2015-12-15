# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimemap', '0003_auto_20151203_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='damaged',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='stolen',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
