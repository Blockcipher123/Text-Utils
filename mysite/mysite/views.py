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
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','Off')
    fullcaps = request.POST.get('fullcaps','Off')
    fullsmall = request.POST.get('fullsmall','Off')
    countchar = request.POST.get('countchar','Off')
    # print(removepunc)
    print(djtext)
    # analyze=djtext
    if removepunc == "on":
        punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''
        analyze = ""
        for i in djtext:
            if i not in punctuations:
                analyze=analyze+i

        params = {'pursose':'Remove Puncations', 'analyzed_text':analyze}
        djtext = analyze
        # return render(request, 'analyze.html', params)
    if (fullcaps=='on'):
        analyze=''
        for i in djtext:
            analyze= analyze+i.upper()
        params = {'pursose':'Changed To Uppercase', 'analyzed_text':analyze}
        djtext = analyze
        # return render(request, 'analyze.html', params)
    if (fullsmall=='on'):
        analyze =''


        
        for i in djtext:
            analyze=analyze+i.lower()
        params = {'pursose':'Changed To LowerCase', 'analyzed_text':analyze}
        djtext = analyze
        # return render(request, 'analyze.html', params)
    
    if (countchar=='on'):
        analyze = ''
        # for i in djtext:
        analyze = len(djtext)

        params = {'pursose':'Count the char', 'countchars':analyze}
        # return render(request, 'analyze.html', params)
    if (removepunc!='on' and fullcaps!='on' and fullsmall!='on' and countchar!='on'):
        return HttpResponse("Pls SELECT any operation!")
    return render(request, 'analyze.html', params)