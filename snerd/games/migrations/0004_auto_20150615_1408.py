# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20150520_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='company',
            field=models.ManyToManyField(to='games.GameCompany', db_table=b'game_to_company', verbose_name=b'company'),
        ),
    ]
