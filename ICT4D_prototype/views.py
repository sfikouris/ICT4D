from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
from ICT4D_prototype.models import Person


def home(request):
    return render(request, 'home.html', {'name' : 'ICT4'})

def add(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    res = num1 + num2
    return render(request, 'result.html', {'result':res})

def data(request):
        name = request.GET['name']
        return HttpResponse(name)

@csrf_exempt
def dummy(request):
    #num1 = request.GET['where']
    myfile = request.POST['recording']
    fs = FileSystemStorage()
    filename = fs.save(myfile, myfile)
    uploaded_file_url = fs.url(filename)
    name = Person(first_name="one", last_name="test", voice = uploaded_file_url)
    name.save()