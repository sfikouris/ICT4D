from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ICT4_prototype-home'),
    path('data', views.data, name='ICT4_prototype-data'),
    path('dummy', views.dummy, name='ICT4_prototype-dummy'),
    path('simple_upload', views.simple_upload, name='ICT4_prototype-simple_upload'),
    path('numberCheck', views.numberCheck, name='ICT4_prototype-numberCheck'),
    path('result', views.result, name='result'),
    path('map', views.map, name='map'),
]
