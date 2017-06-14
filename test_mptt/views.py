#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from test_mptt.models import *
# Create your views here.
def display(foods):
    display_list =[]
    for food in foods:
        display_list.append(food.title)
        print display_list
        print 'hh'
        children = food.children.all()
        print 'children:',children
        if len(children)>0:
            display_list.append(display(food.children.all()))
    print display_list
    return display_list

def unordered_list(request):
    foods = Food.objects.filter(parent=None)
    var = display(foods)
    return render_to_response('unordered_list.html', {'var': var})
