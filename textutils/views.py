from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    
    return render(request,'index.html')

def analyze(request):
    djantext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    fullcaps = request.POST.get('fullcaps','off')
    charcount = request.POST.get('charcount','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if removepunc == "on":
        for char in djantext:
            if char not in punctuations:
                analyzed = analyzed + char
                params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
    elif newlineremove == "on":
        for char in djantext:
            if char!="\n":
                analyzed = analyzed + char
                params = {'purpose':'New Lines Removed','analyzed_text':analyzed}
    elif extraspaceremove == "on":
        for index,char in enumerate(djantext):
            if not(djantext[index]==" " and djantext[index+1]==" "):
                analyzed = analyzed + char
                params = {'purpose':'Extra White Spaces Removed','analyzed_text':analyzed}
    elif fullcaps == "on":
        for char in djantext:
            analyzed = analyzed + char.upper()
            params = {'purpose':'Your text in capitalized format is:','analyzed_text':analyzed}
    elif charcount == "on":
        count = 0
        for char in djantext:
            count = count + 1
        analyzed = count
        params = {'purpose':'Number of characters in your text are:','analyzed_text':analyzed}
    else:
        analyzed = 'Button Not Selected'
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
    return render(request,'analyze.html', params)