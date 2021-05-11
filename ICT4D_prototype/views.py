from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .form import DocumentForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers

import folium


# Create your views here.
from ICT4D_prototype.models import Person
from ICT4D_prototype.models import treeaid
from ICT4D_prototype.models import Document


cercles = ["Sikasso","Koutiala","Bougouni","Kadiolo","Kolondiéba","Yanfolila","Yorosso"]
trees = ["Pterocarpus erinaceus","Terminalia habeensis","Afzelia Africana","Khaya senegalensis","Dalbergia melanoxylon", "Unknown"]


def home(request):
    query_results = treeaid.objects.order_by('phone_number') 
    #query_results = treeaid.objects.all()
    return render(request, 'home.html', {'query_results' : query_results})


def result(request):
    cercle = request.POST['cercle_id']
    tree = request.POST['tree_id']
    phone_number = request.POST['phone_number']
    tree_count = request.POST['tree_num']
    
    data = treeaid()
    data.cercle = cercle
    data.tree = tree
    data.tree_count = tree_count
    data.phone_number = phone_number
    data.save()

    query_results = treeaid.objects.order_by('phone_number') 


    return render(request,"home.html",{'query_results' : query_results})
    
@csrf_exempt
def data(request):
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
        #form.save()
        instance = Document()
        
        phone_number = request.POST['phone']
        
        rec_commune=request.FILES['rec_commune'] = str(phone_number) + str(instance.time)
        rec_location=request.FILES['rec_location']
        caller = request.POST['existingcaller']

        if caller == 0:
            rec_name=request.FILES['rec_name'].name  


        tree_num = int(request.POST['tree_num'])
        tree = trees[tree_num-1]

        cercle_num = int(request.POST['cercle_num'])
        cercle = cercles[cercle_num-1]

        tree_count = request.POST['tree_count']
        chosen_language = request.POST['chosen_language']

        instance.rec_commune = rec_commune
        instance.rec_location = rec_location
        if caller == 0:
            instance.rec_name = rec_name
        instance.cercle_num = cercle
        instance.tree_num = tree
        instance.tree_count = tree_count
        instance.chosen_language = chosen_language
        instance.phone = phone_number
        instance.save()
        return HttpResponse(status=200)
        
   
    return HttpResponse(status=400)


def numberCheck(request):
    phoneNumber = request.GET['phone']
    if Document.objects.filter(phone=phoneNumber).exists():
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


def map(request):
    m = folium.Map(
        location=[45.372, -121.6972],
        zoom_start=12,
        tiles='Stamen Terrain'
    )
    mstring = m._repr_html_()
    context = {'my_map': mstring}

    return render(request, 'map.html', context)

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Document.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)