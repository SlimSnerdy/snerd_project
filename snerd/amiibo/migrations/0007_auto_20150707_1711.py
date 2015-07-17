# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0006_amiibo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amiibo',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
