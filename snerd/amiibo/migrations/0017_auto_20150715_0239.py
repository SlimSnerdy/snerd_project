# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0016_auto_20150708_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amiibo',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media/amiibo/', blank=True),
        ),
    ]
