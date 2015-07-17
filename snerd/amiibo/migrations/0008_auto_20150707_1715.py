# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0007_auto_20150707_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amiibo',
            name='image',
            field=models.ImageField(upload_to=b'amiibo'),
        ),
    ]
