# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_mptt', '0002_auto_20170614_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='tiny',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]
