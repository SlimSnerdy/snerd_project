# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0013_auto_20150707_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amiibo',
            name='image',
        ),
    ]
