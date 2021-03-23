from django.test import TestCase
from django.urls import reverse
from .models import Person, Place, PersonType, PlaceType
from .views import *

# Create your tests here.
class PersonTypeTest(TestCase):
    def setUp(self):
        self.ptype = PersonType(type_name='goblin', type_description='green little bastard')

    def test_string(self):
        self.assertEqual(str(self.ptype), 'goblin')
    
    def test_table(self):
        self.assertEqual(str(PersonType._meta.db_table), 'persontype')
        self.assertEqual(str(PersonType._meta.verbose_name_plural), 'persontypes')


class PersonTest(TestCase):
    def setUp(self):
        self.apersontype = PersonType(type_name='wizard', type_description='hoarding all the XP')
        self.aperson = Person(  name='Tom Bombadil', 
                                person_type=self.apersontype,
                                description='lived in a forest and didn\'t make the cut for the movie')
               
    def test_string(self):
        self.assertEqual(str(self.aperson), 'Tom Bombadil')
    
    def test_table(self):
        self.assertEqual(str(Person._meta.db_table), 'person')
        self.assertEqual(str(Person._meta.verbose_name_plural), 'people')

class PlaceTypeTest(TestCase):
    def setUp(self):
        self.pltype = PlaceType(type_name='Morgue', type_description='a cold, desolate place.')

    def test_string(self):
        self.assertEqual(str(self.pltype), 'Morgue')
    
    def test_table(self):
        self.assertEqual(str(PlaceType._meta.db_table), 'placetype')
        self.assertEqual(str(PlaceType._meta.verbose_name_plural), 'placetypes')

class PlaceTest(TestCase):
    def setUp(self):
        self.aplacetype = PlaceType(type_name='Nest', type_description='A place for children and treasure')
        self.aplace = Place(  name='Widow\'s peak', 
                                place_type=self.aplacetype,
                                description='A nest at the farthest north peak.')
               
    def test_string(self):
        self.assertEqual(str(self.aplace), 'Widow\'s peak')
    
    def test_table(self):
        self.assertEqual(str(Place._meta.db_table), 'place')
        self.assertEqual(str(Place._meta.verbose_name_plural), 'places')

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class PersonDetailsViewTest(TestCase):
    def setUp(self):
        self.test_person_type = PersonType.objects.create(type_name='wizard', type_description='hoarding all the XP')
        self.test_person = Person.objects.create(name='Tom Bombadil', 
                                person_type=self.test_person_type,
                                description='lived in a forest and didn\'t make the cut for the movie')

    def test_person_detail_success(self):
        response = self.client.get(reverse('persondetails', args=(self.test_person.id,)))
        self.assertEqual(response.status_code, 200)

#updated
