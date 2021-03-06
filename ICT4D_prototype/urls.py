from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ICT4_prototype-home'),
    path('home', views.home, name='ICT4_prototype-home'),
    path('data', views.data, name='ICT4_prototype-data'),
    path('simple_upload', views.simple_upload, name='ICT4_prototype-simple_upload'),
    path('numberCheck', views.numberCheck, name='ICT4_prototype-numberCheck'),
    path('result', views.result, name='result'),
    path('map', views.map, name='map'),
    path('dashboard', views.dashboard_with_pivot, name="dashboard_with_pivot"),
    path('dashboardata', views.pivot_data, name='pivot_data'),
]
