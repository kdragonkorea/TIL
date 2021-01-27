from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def exercise1(request) :
    template = loader.get_template('exercise1.html')
    name = 'alex'
    context = {"result":name}
    return HttpResponse(template.render(context, request))

def exercise2(request) :
    if request.method == 'POST':
        writer = request.POST['text']
        opinion = request.POST['textarea']
        context = {'writer':writer, 'opinion':opinion}
    else:
        context = None
    return render(request, 'exercise2.html', context)