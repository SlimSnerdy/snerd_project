# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecream',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'flavor'),
        ),
    ]