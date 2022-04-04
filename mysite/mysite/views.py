# This is my Block_Cipher file 
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = {'Name':'Block_Cipher','Programmng_Language':'Python'}

    return render(request,'index.html')

    # return HttpResponse("HOME")


def analyze(request):
    # Geting the text
    # print(request.GET.get('text','default'))
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','Off')
    fullcaps = request.GET.get('fullcaps','Off')
    fullsmall = request.GET.get('fullsmall','Off')
    countchar = request.GET.get('countchar','Off')
    print(removepunc)
    print(djtext)
    # analyze=djtext
    if removepunc == "on":
        punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''
        analyze = ""
        for i in djtext:
            if i not in punctuations:
                analyze=analyze+i

        params = {'pursose':'Remove Puncations', 'analyzed_text':analyze}
        return render(request, 'analyze.html', params)
    elif (fullcaps=='on'):
        analyze=''
        for i in djtext:
            analyze= analyze+i.upper()
        params = {'pursose':'Changed To Uppercase', 'analyzed_text':analyze}
        return render(request, 'analyze.html', params)
    elif (fullsmall=='on'):
        analyze =''
        for i in djtext:
            analyze=analyze+i.lower()
        params = {'pursose':'Changed To LowerCase', 'analyzed_text':analyze}
        return render(request, 'analyze.html', params)
    
    elif (countchar=='on'):
        analyze = ''
        # for i in djtext:
        analyze = len(djtext)

        params = {'pursose':'Count the char', 'countchars':analyze}
        return render(request, 'analyze.html', params)
            


    else:
        return HttpResponse('<h1>Error! Plese click on Remove Puncatations ^__^</h1>')