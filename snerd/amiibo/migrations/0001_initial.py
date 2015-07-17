# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amiibo',
            fields=[
                ('amiibo_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'character')),
                ('rating', models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True)),
            ],
            options={
                'db_table': 'amiibo',
                'verbose_name_plural': 'amiibo',
            },
        ),
        migrations.CreateModel(
            name='AmiiboSeries',
            fields=[
                ('amiibo_series_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'amiibo_series',
                'verbose_name_plural': 'amiibo series',
            },
        ),
        migrations.CreateModel(
            name='AmiiboUniverse',
            fields=[
                ('amiibo_universe_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'amiibo_universe',
            },
        ),
        migrations.AddField(
            model_name='amiibo',
            name='series',
            field=models.ForeignKey(to='amiibo.AmiiboSeries'),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='universe',
            field=models.ForeignKey(to='amiibo.AmiiboUniverse'),
        ),
    ]
