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
#import datetime
import folium


from ICT4D_prototype.models import treeaid_databese
from ICT4D_prototype.models import Document


cercles = ["Sikasso","Koutiala","Bougouni","Kadiolo","Kolondiéba","Yanfolila","Yorosso"]
trees = ["Pterocarpus erinaceus","Terminalia habeensis","Afzelia Africana","Khaya senegalensis","Dalbergia melanoxylon", "Unknown"]

#the home page of the application (non admin)
def home(request):
    query_results = treeaid_databese.objects.order_by('phone_number') 
    query_results_phone = Document.objects.order_by('phone') 

    context = {
    "query_results" : query_results ,
    "query_results_phone" : query_results_phone
    }
    return render(request, 'home.html', context)

#the table that stores and takes in web reported trees.
def result(request):
    cercle = request.POST['cercle_id']
    tree = request.POST['tree_id']
    phone_number = request.POST['phone_number']
    tree_count = request.POST['tree_num']
    
    data = treeaid_databese()
    data.cercle = cercle
    data.tree = tree
    data.tree_count = tree_count
    data.phone_number = phone_number
    data.save()

    query_results = treeaid_databese.objects.order_by('phone_number') 
    query_results_phone = Document.objects.order_by('phone') 
    context = {
    "query_results" : query_results ,
    "query_results_phone" : query_results_phone
    }

    return render(request,"home.html",context)

#the webpage set-up for recieving post messages from the vxml server
@csrf_exempt
def data(request):
    form = DocumentForm(request.POST, request.FILES)
    #if form.is_valid():

    instance = Document()
        
    rec_commune=request.FILES['rec_commune']
    rec_location=request.FILES['rec_location']
    caller = request.POST['existingcaller']
    #if caller == 0:
    rec_name=request.FILES['rec_name']


    tree_num = int(request.POST['tree_num'])
    tree = trees[tree_num-1]

    cercle_num = int(request.POST['cercle_num'])
    cercle = cercles[cercle_num-1]

    tree_count = request.POST['tree_count']
    chosen_language = request.POST['chosen_language']
    phone_number = request.POST['phone']

    #x = datetime.datetime.now()
    #rec_commune.name = str(phone_number) + str(x.hour) + str(x.minute)
    #src_commune = "media/commune/" + rec_commune.name + ".wav"

    instance.rec_commune = rec_commune
    instance.rec_location = rec_location
    #if caller == 0:
    instance.rec_name = rec_name
    instance.cercle_num = cercle
    instance.tree_num = tree
    instance.tree_count = tree_count
    instance.chosen_language = chosen_language
    instance.phone = phone_number
    #instance.src_commune = src_commune
    instance.save()
    return HttpResponse(status=200)
        
   
    #return HttpResponse(status=400)

#the page that returns a 404 response if the caller is not yet in the database. Within the vxml this event is handled
def numberCheck(request):
    phoneNumber = request.GET['phone']
    if Document.objects.filter(phone=phoneNumber).exists():
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)

#the form to upload data on the web
@csrf_exempt
def simple_upload(request):
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return HttpResponse(status=200)
    
#the map, uses the folium plugin.
def map(request):
    m = folium.Map(
        location=[45.372, -121.6972],
        zoom_start=12,
        tiles='Stamen Terrain'
    )
    mstring = m._repr_html_()
    context = {'my_map': mstring}

    return render(request, 'map.html', context)

#the dashboard function
def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Document.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)