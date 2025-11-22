from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
def sample(request):
    return HttpResponse("welcome to django")

def basic(request):
    return HttpResponse("hey dude! Whats-app")

def calc(request):
    a=int(request.GET.get('a'))
    b=int(request.GET.get('b'))
    op=request.GET.get('op')
    if(op=='+'):
        return HttpResponse(a+b)
    elif(op=='-'):
        return HttpResponse(a-b)
    elif(op=='*'):
        return HttpResponse(a*b)
    elif(op=='/'):
        return HttpResponse(a/b)
    elif(op=='%'):
        return HttpResponse(a%b)
    elif(op=='//'):
        return HttpResponse(a//b)
    else:
        return HttpResponse('invalid operator')