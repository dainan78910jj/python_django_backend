from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App </em>")

def help(request):
    # return HttpResponse("<em> My Help </em>")
    my_dict = {'insert_me': "Hello i am from view.py!"}
    return render(request, 'index.html', context=my_dict)

