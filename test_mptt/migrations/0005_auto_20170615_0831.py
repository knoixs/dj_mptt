# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('test_mptt', '0004_ckedit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ckedit',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u5185\u5bb9'),
        ),
    ]
