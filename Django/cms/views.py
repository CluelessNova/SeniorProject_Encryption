from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index1.html', {})


def encrypt(request):
    # return HTTPResponse('encrypt')
    return render(request, 'encrypt.html')

def decrypt(request):
    # return HTTPResponse('encrypt')
    return render(request, 'decrypt.html')


def thesis(request):
    # return HTTPResponse('encrypt')
    return render(request, 'thesis.html')
