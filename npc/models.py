from django.db import models
from django.contrib.auth.models import User

class PersonType(models.Model):
    type_name = models.CharField(max_length=255)
    type_description = models.TextField()

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'persontype'
        verbose_name_plural = 'persontypes'

class Person(models.Model):
    name = models.CharField(max_length=255)
    person_type = models.ForeignKey(PersonType, on_delete = models.DO_NOTHING)
    description = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'person'
        verbose_name_plural = 'people'

class PlaceType(models.Model):
    type_name = models.CharField(max_length=255)
    type_description = models.TextField()

        
    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'placetype'
        verbose_name_plural = 'placetypes'

class Place(models.Model):
    name = models.CharField(max_length=255)
    place_type = models.ForeignKey(PlaceType, on_delete = models.DO_NOTHING)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'place'
        verbose_name_plural = 'places'
