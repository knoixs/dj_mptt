# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='test_mptt.Food', null=True)),
            ],
        ),
    ]
