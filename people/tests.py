from django.core.validators import ValidationError
from django.test import TestCase
from datetime import date
from people.models import Person

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
    def test_saving_and_retrieving_people(self):
        person = Person()

        person.title = "Herr"
        person.name_or_company = "Mustermann"
        person.surname = "Max"
        person.birthday = date(2023, 5, 19)

        person.save()

        saved_people = Person.objects.all()
        self.assertEqual(saved_people.count(), 1)

        saved_person = saved_people[0]

        self.assertEqual(saved_person.title, "Herr")
        self.assertEqual(saved_person.name_or_company, "Mustermann")
        self.assertEqual(saved_person.surname, "Max")
        self.assertEqual(saved_person.birthday, date(2023, 5, 19))

    def test_valitadion_of_title_field(self):
        person = Person(title="FooBar")

        self.assertValidationError(
            person,
            "title",
            "Value 'FooBar' is not a valid choice.")
