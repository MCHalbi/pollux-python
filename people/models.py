from django.db import models

class Adress(models.Model):
    street = models.CharField(max_length=255, default="")
    postal_code = models.CharField(max_length=31, default="")
    city = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=255, default="")

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
    date_of_birth = models.DateField(null=True, default=None)

    adress = models.ForeignKey(Adress, on_delete=models.CASCADE,
                               default=Adress.objects.create)
