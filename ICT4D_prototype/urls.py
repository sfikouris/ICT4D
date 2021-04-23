from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ICT4_prototype-home'),
    path('data/', views.data, name='ICT4_prototype-data'),
    path('dummy', views.dummy, name='ICT4_prototype-dummy'),
    path('simple_upload', views.simple_upload, name='ICT4_prototype-simple_upload'),
   
]
