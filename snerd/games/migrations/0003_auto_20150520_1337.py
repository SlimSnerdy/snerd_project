# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20150313_1539'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gamecompany',
            options={'verbose_name_plural': 'Game companies'},
        ),
    ]
