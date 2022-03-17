# This is my Block_Cipher file 
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = {'Name':'Block_Cipher','Programmng_Language':'Python'}

    return render(request,'index.html')

    # return HttpResponse("HOME")


def removepunc(request):
    # Geting the text
    # print(request.GET.get('text','default'))
    djtext = request.GET.get('text','default')
    print(djtext)
    # Analyze the text 
    return HttpResponse("Remove Punc")

def capfirst(request):
    return HttpResponse("capfirst")

def newline(request):
    return HttpResponse("NewLine Page")

def spaceremover(request):
    return HttpResponse("Spaceremove Page")

def charcount(request):
    return HttpResponse("charcount Page")

