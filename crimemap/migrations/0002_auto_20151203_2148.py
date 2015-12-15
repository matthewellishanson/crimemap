# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimemap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='end',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='start',
            field=models.DateField(null=True, blank=True),
        ),
    ]
