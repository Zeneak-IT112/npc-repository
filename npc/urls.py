from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('person_type/', views.person_type, name='persontypes'),
    path('place_type/', views.place_type, name='placetypes'),
]