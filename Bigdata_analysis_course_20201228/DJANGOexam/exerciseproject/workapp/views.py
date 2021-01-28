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
        writer = request.POST['text']   # html에서 name 값은 text
        opinion = request.POST['textarea']  # html에서 name 값은 textarea
        context = {'writer':writer, 'opinion':opinion}
    else:
        context = None  # 템플릿에 전달할거 없을 때
    return render(request, 'exercise2.html', context)

def product1(request) :
    return render(request, 'product1.html', None)

def basket1(request, uri) :
    request.method == 'GET'
    context = {'uri':uri}
    return render(request, 'basket1.html', context)