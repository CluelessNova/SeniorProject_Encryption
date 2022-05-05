from django.shortcuts import render
from django.http import HttpResponse
from . import encryptCode

def index(request):
    return render(request, 'index.html', {})

def decrypt(request):
    return render(request, 'decrypt.html', {})

def encrypt(request):
    return render(request, 'encrypt.html', {})

def thesis(request):
    return render(request, 'thesis.html', {})

def genKey(request):
    result = encryptCode.key(request.GET.get('num', '0'))
    return HttpResponse(result)

def encryptMess(request):
    mess = request.GET.get('mess', '')
    key = request.GET.get('key', '1')
    result = encryptCode.encryptMess(key, mess)
    return HttpResponse(result)

def decryptMess(request):
    mess = request.GET.get('mess', '')
    key = request.GET.get('key', '1')
    result = encryptCode.decryptMess(key, mess)
    return HttpResponse(result)

