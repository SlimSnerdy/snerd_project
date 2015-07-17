# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0005_remove_amiibo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiibo',
            name='image',
            field=models.ImageField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
