from django.db import models

class Person(models.Model):
    title = models.CharField(
        max_length=5,
        choices=[
            ("Herr", "Herr"),
            ("Frau", "Frau"),
            ("Firma", "Firma"),
            ],
    )
    name_or_company = models.CharField(max_length=255, default="")
    surname = models.CharField(max_length=255, default="")
    date_of_birth = models.DateField()
