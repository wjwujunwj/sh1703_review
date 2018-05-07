from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):

    return HttpResponse('hello word!')





def hello_tpl(request):
    tpl='todos/hello_tpl.html'

    arr=[
        {'id':'1','name':'a'},
        {'id': '2', 'name': 'b'},
        {'id': '3', 'name': 'c'},
        {'id': '4', 'name': 'd'}
    ]
    info={'arr':arr}
    ret=render(request,tpl,info)
    return ret