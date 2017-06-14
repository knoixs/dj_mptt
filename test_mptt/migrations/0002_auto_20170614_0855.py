# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_mptt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MPTTFood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', models.ForeignKey(related_name='children', verbose_name='\u8d77\u6e90', blank=True, to='test_mptt.MPTTFood', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='food',
            name='parent',
            field=models.ForeignKey(related_name='children', verbose_name='\u8d77\u6e90', blank=True, to='test_mptt.Food', null=True),
        ),
    ]
