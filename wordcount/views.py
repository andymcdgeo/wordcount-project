from django.http import HttpResponse
from django.shortcuts import render
import operator
import re

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['FullText']

    #wordlist = fulltext.split()
    #wordlist = re.split('[-,. |--]', fulltext)
    test = re.compile(r'\w+(?:-\w+)*')
    wordlist = re.findall(test, fulltext)

    commonwords = {}
    print(test)
    for word in wordlist:
        if word in commonwords:
            #Increase 
            commonwords[word] += 1
        else:
            #Add to the dictionary
            commonwords[word] = 1

    sorted_commonwords = sorted(commonwords.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sorted_commonwords':sorted_commonwords})

def about(request):
    return render(request, 'about.html')