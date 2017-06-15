# -*-coding:utf-8-*-

from django.db import models
from mptt.models import MPTTModel
from tinymce.models import HTMLField
# from uploader.models import
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

# 测试unordered_list
class Food(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', verbose_name=u'起源')

    def __unicode__(self):
        return self.title


# 测试django_mptt
class MPTTFood(MPTTModel):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True, related_name="children", verbose_name=u'起源')

    def __unicode__(self):
        return self.title


# 测试tinymce
class tiny(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=50)
    content = HTMLField()

    def __unicode__(self):
        return self.title


# 测试ckeditor
class ckedit(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=50)
    content = RichTextUploadingField(verbose_name=u'内容')

    def __unicode__(self):
        return self.title
