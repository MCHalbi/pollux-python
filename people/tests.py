from django.core.validators import ValidationError
from django.test import TestCase
from datetime import date
from people.models import Person, Adress

class TestValidationErrorMixin:
    def assertValidationError(self, model_object, field_name, message=None):
        try:
            model_object.full_clean()
        except ValidationError as e:
            self.assertTrue(
                field_name in e.message_dict,
                f"The value \"{getattr(model_object, field_name)}\" of "
                + f"field \"{field_name}\" should be invalid, but it was not.")
            if message:
                self.assertEqual(
                    e.message_dict[field_name][0], message)

class PeopleModelTest(TestCase, TestValidationErrorMixin):
    def test_saving_and_retrieving_person(self):
        person = Person()

        person.title = "Herr"
        person.name_or_company = "Mustermann"
        person.surname = "Max"
        person.date_of_birth = date(2023, 5, 19)

        adress = Adress()

        adress.street = "Musterstraße 123"
        adress.postal_code = "12345"
        adress.city = "Musterstadt"
        adress.country = "Musterland"

        adress.save()

        person.adress = adress

        person.save()

        saved_people = Person.objects.all()
        self.assertEqual(saved_people.count(), 1)

        saved_person = saved_people[0]

        self.assertEqual(saved_person.title, "Herr")
        self.assertEqual(saved_person.name_or_company, "Mustermann")
        self.assertEqual(saved_person.surname, "Max")
        self.assertEqual(saved_person.date_of_birth, date(2023, 5, 19))

        self.assertEqual(saved_person.adress, adress)

    def test_default_person_has_all_empty_fields(self):
        person = Person()
        person.save()

        self.assertEqual(person.title, "")
        self.assertEqual(person.name_or_company, "")
        self.assertEqual(person.surname, "")
        self.assertEqual(person.date_of_birth, None)

        self.assertEqual(person.adress.street, "")
        self.assertEqual(person.adress.postal_code, "")
        self.assertEqual(person.adress.city, "")
        self.assertEqual(person.adress.country, "")


    def test_valitadion_of_title_field(self):
        person = Person(title="FooBar")

        self.assertValidationError(
            person,
            "title",
            "Value 'FooBar' is not a valid choice.")

class AdressModelTest(TestCase):
    def test_saving_and_retrieving_adress(self):
        adress = Adress()

        adress.street = "Musterstraße 123"
        adress.postal_code = "12345"
        adress.city = "Musterstadt"
        adress.country = "Musterland"

        adress.save()

        saved_adresses = Adress.objects.all()
        self.assertEqual(saved_adresses.count(), 1)

        saved_adress = saved_adresses[0]

        self.assertEqual(saved_adress.street, "Musterstraße 123")
        self.assertEqual(saved_adress.postal_code, "12345")
        self.assertEqual(saved_adress.city, "Musterstadt")
        self.assertEqual(saved_adress.country, "Musterland")
