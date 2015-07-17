# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('release_date', models.DateField(null=True)),
                ('rating', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
            options={
                'db_table': 'game',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameCompany',
            fields=[
                ('company_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'game_company',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameCompanyRole',
            fields=[
                ('role_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'game_company_role',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GamePlatform',
            fields=[
                ('platform_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'game_platform',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gamecompany',
            name='role',
            field=models.ManyToManyField(to='games.GameCompanyRole', db_table=b'game_company_to_role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='company',
            field=models.ManyToManyField(to='games.GameCompany', db_table=b'game_to_company'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ManyToManyField(to='games.GamePlatform', db_table=b'game_to_platform'),
            preserve_default=True,
        ),
    ]
