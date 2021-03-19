from django.contrib import admin
from .models import PersonType, Person, PlaceType, Place

admin.site.register(PersonType)
admin.site.register(Person)
admin.site.register(PlaceType)
admin.site.register(Place)

# Register your models here.
