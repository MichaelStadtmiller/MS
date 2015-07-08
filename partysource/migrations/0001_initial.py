# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('myclass', models.CharField(max_length=50)),
                ('style1', models.CharField(max_length=50)),
                ('style2', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('ABV', models.DecimalField(max_digits=4, decimal_places=1)),
                ('size', models.IntegerField(default=0)),
                ('UOM', models.CharField(max_length=10)),
                ('mytype', models.CharField(max_length=20)),
                ('cost', models.DecimalField(max_digits=5, decimal_places=2)),
                ('QOH', models.IntegerField(default=0)),
            ],
        ),
    ]
