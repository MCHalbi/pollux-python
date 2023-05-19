from django.core.validators import ValidationError
from django.test import TestCase
from datetime import date
from people.models import Person

class PeopleModelTest(TestCase):
    def test_saving_and_retrieving_people(self):
        person = Person()
        person.title = "Herr"
        person.name = "Mustermann"
        person.surname = "Max"
        person.birthday = date(2023, 5, 19)
        person.save()

        saved_people = Person.objects.all()
        self.assertEqual(saved_people.count(), 1)

        saved_person = saved_people[0]

        self.assertEqual(saved_person.title, "Herr")
        self.assertEqual(saved_person.name, "Mustermann")
        self.assertEqual(saved_person.surname, "Max")
        self.assertEqual(saved_person.birthday, date(2023, 5, 19))

    def test_valitadion_of_title_field(self):
        person = Person(title="FooBar")

        try:
            person.full_clean()
        except ValidationError as e:
            self.assertTrue(
                "title" in e.message_dict,
                "The value of \"title\" should be invalid, but it was not.")
