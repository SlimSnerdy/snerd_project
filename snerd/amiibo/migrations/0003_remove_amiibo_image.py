# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0002_amiibo_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amiibo',
            name='image',
        ),
    ]
