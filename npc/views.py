from .models import Person, PersonType, Place, PlaceType
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'npc/index.html')

def person_type(request):
    person_type_list=PersonType.objects.all()
    return render(request, 'npc/persontypes.html' ,{'person_type_list' : person_type_list})

def place_type(request):
    place_type_list=PlaceType.objects.all()
    return render(request, 'npc/placetypes.html' ,{'place_type_list' : place_type_list})

def person(request):
     people_list = Person.objects.all()
     return render(request, 'npc/person.html', {'people_list' : people_list})