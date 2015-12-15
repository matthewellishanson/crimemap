# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimemap', '0002_auto_20151203_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='reported',
            field=models.DateField(null=True, blank=True),
        ),
    ]
