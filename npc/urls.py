from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('persontypes/', views.person_type, name='persontypes'),
    path('placetypes/', views.place_type, name='placetypes'),
    path('personlist/', views.person_list, name='personlist'),
    path('persondetails/<int:id>', views.person_details, name='persondetails'),
    path('placelist/', views.place_list, name ='placelist'),
    path('placedetails/<int:id>', views.place_details, name = 'placedetails'),
    path('newperson/', views.newPerson, name = 'newperson'),
    path('newplace/', views.newPlace, name = 'newplace'),
]