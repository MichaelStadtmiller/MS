# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partysource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottle',
            name='ABV',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='bottle',
            name='QOH',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bottle',
            name='UOM',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AddField(
            model_name='bottle',
            name='age',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AddField(
            model_name='bottle',
            name='brand',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='bottle',
            name='cat',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='bottle',
            name='classi',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='bottle',
            name='container',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='bottle',
            name='desc',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AddField(
            model_name='bottle',
            name='img',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='bottle',
            name='origin',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='bottle',
            name='package',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='bottle',
            name='price',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='bottle',
            name='prodtype',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='bottle',
            name='region',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='bottle',
            name='retail',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='bottle',
            name='size',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='bottle',
            name='style1',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='bottle',
            name='style2',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='bottle',
            name='name',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
