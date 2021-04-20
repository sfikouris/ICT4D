from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> Home page </h1>')

def data(request):
        if request == 'GET':
            name = request.GET['name']
        print(name)