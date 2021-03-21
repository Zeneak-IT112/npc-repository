from django.test import TestCase
from .models import Person, Place, PersonType, PlaceType

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

