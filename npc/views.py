from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import PersonForm, PlaceForm
from .models import Person, PersonType, Place, PlaceType

# Create your views here.
def index (request):
    return render(request, 'npc/index.html')

def person_type(request):
    person_type_list = PersonType.objects.all()
    return render(request, 'npc/persontypes.html' ,{'person_type_list' : person_type_list})

def place_type(request):
    place_type_list = PlaceType.objects.all()
    return render(request, 'npc/placetypes.html' ,{'place_type_list' : place_type_list})

def person_list(request):
     people_list = Person.objects.all()
     return render(request, 'npc/personlist.html', {'people_list' : people_list})

def person_details(request, id):
    person_details = get_object_or_404(Person, pk=id)
    return render(request, 'npc/persondetails.html', {'person_details': person_details})

def place_list(request):
    place_list = Place.objects.all()
    return render(request, 'npc/placelist.html', {'place_list' : place_list})

def place_details(request, id):
    place_details = get_object_or_404(Place, pk=id)
    return render(request, 'npc/placedetails.html', {'place_details' : place_details})

@login_required
def newPerson(request):
     form = PersonForm
     if request.method == 'POST':
          form = PersonForm(request.POST)
          if form.is_valid():
               post = form.save(commit=True)
               post.save()
               form = PersonForm()
     else:
          form = PersonForm()
     return render(request, 'npc/newperson.html', {'form': form})

@login_required
def newPlace(request):
     form = PlaceForm
     if request.method == 'POST':
          form = PlaceForm(request.POST)
          if form.is_valid():
               post = form.save(commit=True)
               post.save()
               form = PlaceForm()
     else:
          form = PlaceForm()
     return render(request, 'npc/newplace.html', {'form': form})

def loginmessage(request):
     return render(request, 'npc/loginmessage.html')

def logoutmessage(request):
     return render(request, 'npc/logoutmessage.html')