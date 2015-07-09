# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partysource', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bottle',
            old_name='brand',
            new_name='classi',
        ),
        migrations.RenameField(
            model_name='bottle',
            old_name='cost',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='bottle',
            name='ABV',
        ),
        migrations.RemoveField(
            model_name='bottle',
            name='UOM',
        ),
        migrations.RemoveField(
            model_name='bottle',
            name='age',
        ),
        migrations.RemoveField(
            model_name='bottle',
            name='category',
        ),
        migrations.RemoveField(
            model_name='bottle',
            name='myclass',
        ),
        migrations.RemoveField(
            model_name='bottle',
            name='mytype',
        ),
        migrations.RemoveField(
            model_name='bottle',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='bottle',
            name='region',
        ),
        migrations.RemoveField(
            model_name='bottle',
            name='style1',
        ),
        migrations.RemoveField(
            model_name='bottle',
            name='style2',
        ),
    ]
