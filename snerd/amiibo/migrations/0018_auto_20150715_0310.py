# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0017_auto_20150715_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amiibo',
            name='image',
            field=models.ImageField(null=True, upload_to=b'amiibo/', blank=True),
        ),
    ]
