#-*-coding:utf-8-*-
from django.db import models
from mptt.models import MPTTModel

# Create your models here.

#测试unordered_list
class Food(models.Model):
    title = models.CharField(verbose_name=u'标题',max_length=50)
    parent = models.ForeignKey('self',blank=True,null=True,related_name='children',verbose_name=u'起源')

    def __unicode__(self):
        return self.title

#测试django_mptt
class MPTTFood(MPTTModel):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self',blank=True,null=True,related_name="children",verbose_name=u'起源')

    def __unicode__(self):
        return self.title
