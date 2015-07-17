# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('ice_cream_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('rating', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
            options={
                'db_table': 'ice_cream',
            },
        ),
        migrations.CreateModel(
            name='IceCreamBrand',
            fields=[
                ('ice_cream_brand_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'ice_cream_brand',
            },
        ),
        migrations.AddField(
            model_name='icecream',
            name='brand',
            field=models.ForeignKey(to='ice_cream.IceCreamBrand'),
        ),
    ]
