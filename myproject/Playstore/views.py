from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

def index5(request):
    return HttpResponse("<h1>Hi, Good Morning.</h1>")
def index6(request):
    return HttpResponse("<h1>Hi, My Name is Dhruv.</h1>")
def index7(request):
    return HttpResponse("<h1>I recently completed my Senior Secondary Education from C.B.S.E Board.</h1>")
def index8(request):
    return HttpResponse("<h1>I am from Ambala City.</h1>")

def mno(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())
