from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def koti(request):
    return HttpResponse('koti is a good boy')
def vinay(request):
    return HttpResponse('vinay is python developer')
def vicky(request):
    return HttpResponse('now we are all learn english')
def krish(request):
    return HttpResponse('we are all python students in jspyders')
