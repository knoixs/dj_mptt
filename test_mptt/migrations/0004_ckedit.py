# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('test_mptt', '0003_tiny'),
    ]

    operations = [
        migrations.CreateModel(
            name='ckedit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'contents')),
            ],
        ),
    ]
