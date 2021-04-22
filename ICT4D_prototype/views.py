from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from ICT4D_prototype.models import Person
from ICT4D_prototype.models import treeaid

cercles = ["Bougouni","Kadiolo","Kolondieba","Koutiala","Skasso","Yanfolila","Yorosso"]
trees = ["Pterocarpus erinaceus","Terminalia habeensis","Afzelia Africana","Khaya senegalensis","Dalbergia melanoxylon", "Unknown"]

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
    cercle_num = int(request.GET['cercle_num'])
    cercle = cercles[cercle_num-1]

    tree_num = int(request.GET['tree_num'])
    tree = trees[tree_num-1]

    tree_count = int(request.GET['tree_count'])

    data = treeaid()
    data.cercle = cercle
    data.tree = tree
    data.tree_count = tree_count
    data.save()
    return render(request, 'home.html', {'name' : 'ICT4'})


    #num1 = request.GET['where']
    #record = request.POST.get('voice', False)
    #name = Person(first_name="one", last_name="test", voice = record)
    #name.save()
    #return HttpResponse("HI")