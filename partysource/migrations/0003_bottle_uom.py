# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partysource', '0002_auto_20150709_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottle',
            name='UOM',
            field=models.CharField(default='ML', max_length=10),
            preserve_default=False,
        ),
    ]
