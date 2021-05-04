from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .form import DocumentForm


# Create your views here.
from ICT4D_prototype.models import Person
from ICT4D_prototype.models import treeaid

cercles = ["Sikasso","Koutiala","Bougouni","Kadiolo","Kolondiéba","Yanfolila","Yorosso"]
trees = ["Pterocarpus erinaceus","Terminalia habeensis","Afzelia Africana","Khaya senegalensis","Dalbergia melanoxylon", "Unknown"]

def home(request):
    query_results = treeaid.objects.all()
    return render(request, 'home.html', {'query_results' : query_results})


def result(request):
    cercle = request.GET['cercle_id']
    tree = request.GET['tree_id']
    phone_number = request.GET['phone_number']
    tree_count = request.GET['tree_num']
    
    data = treeaid()
    data.cercle = cercle
    data.tree = tree
    data.tree_count = tree_count
    data.phone_number = phone_number
    data.save()

    query_results = treeaid.objects.all()

    return render(request,"home.html",{'query_results' : query_results})

def data(request):
        name = request.GET['name']
        return HttpResponse(name)

def numberCheck(request):
    phoneNumber = request.GET['phone']
    if treeaid.objects.filter(phone_number=phoneNumber).exists():
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)

@csrf_exempt
def simple_upload(request):
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return HttpResponse(status=200)
    

@csrf_exempt
def dummy(request):
    cercle_num = int(request.GET['cercle_num'])
    cercle = cercles[cercle_num-1]

    tree_num = int(request.GET['tree_num'])
    tree = trees[tree_num-1]

    tree_count = int(request.GET['tree_count'])

    phone_number = request.GET['phone']

    data = treeaid()
    data.cercle = cercle
    data.tree = tree
    data.tree_count = tree_count
    data.phone_number = phone_number
    data.save()
    return HttpResponse(status=200)

    #return render(request, 'home.html', {'name' : 'ICT4'})


    #num1 = request.GET['where']
    #record = request.POST.get('voice', False)
    #name = Person(first_name="one", last_name="test", voice = record)
    #name.save()
    #return HttpResponse("HI")