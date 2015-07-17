# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0011_remove_amiibo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiibo',
            name='image',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
