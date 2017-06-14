#-*-coding:utf-8-*-
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from test_mptt.models import *
# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id','title')

@admin.register(MPTTFood)
class MPTTFoodAdmin(MPTTModelAdmin):
    list_display = ('id','title','parent')


# admin.site.register(MPTTFood, MPTTModelAdmin)