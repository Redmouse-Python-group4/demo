from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
import datetime

# Create your views here.
def get_now(request, page=1):
    now=datetime.datetime.now()
    html_str = "<html><head><head><body>%s number %s</body></html>"%(now, page)
    html_str = "kfhdjhfdjhfjdfjh"
    return HttpResponse(html_str)

def get_now_2(request, page=1):
    now=datetime.datetime.now()
    print request.get_host()
    if request.method=='GET':
            pages = [{'id': 123, 'title': 'hjhj'}, {'id': 22, 'title': 'wwhjhjw'}]
    for i in request.GET:
        pages.append({"id": i, 'title': request.GET[i]})
    return render(request, 'index.html', {'pages': pages})

def get_now_3(request, page=1):
    now=datetime.datetime.now()
    pages = [{'id': 123, 'title': 'hjhj'}, {'id': 22, 'title': 'wwhjhjw'}]
    return render_to_response('index.html', {'pages': pages})

def google(request):
    return redirect('http://google.kg')