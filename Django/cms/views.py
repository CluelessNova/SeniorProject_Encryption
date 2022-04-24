from django.http import HttpResponse
from django.shortcuts import render
from . import hello, encryption

def index(request):
    return render(request, 'index.html', {})

def encrypt(request):
    # return HTTPResponse('encrypt')
    return render(request, 'encrypt.html')

def decrypt(request):
    # return HTTPResponse('encrypt')
    return render(request, 'decrypt.html')


def thesis(request):
    # return HTTPResponse('encrypt')
    return render(request, 'thesis.html')


def printHelloInConsole(request):

    result = hello.key(request.GET.get('num', '0'))
    return HttpResponse(result)

def encryptMess(request):
    mess = request.GET.get('mess', '')
    key = request.GET.get('key', '1')
    result = hello.encryptMess(key, mess)
    return HttpResponse(result)