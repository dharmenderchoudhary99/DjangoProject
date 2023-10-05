# Created file

from django.http import HttpResponse
from django.shortcuts import render


## Videos 6
# def index(request):
#     return HttpResponse("<h1>Hello</h1>")
#
# def about(request):
#     return HttpResponse("About me")

def index(request):
    params = {'name': 'Dharm', 'Place': 'Prem Ma 969ndir'}
    return render(request, 'index.html', params)
    # return HttpResponse("<h1>Dharmender</h1>")


# def removepunc(request):
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("Remove Punc")
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check the checkbox
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    # analyzed = djtext
    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removing Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not djtext[index] == " " and djtext[index + 1] == " ":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != "/r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (charcounter == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = str(len(djtext))
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")


def capfirst(request):
    return HttpResponse("Capitalize first")
