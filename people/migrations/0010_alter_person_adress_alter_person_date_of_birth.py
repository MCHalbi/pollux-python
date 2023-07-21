# Generated by Django 4.2.1 on 2023-07-21 21:59

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query


class Migration(migrations.Migration):
    dependencies = [
        ("people", "0009_alter_person_adress"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="adress",
            field=models.ForeignKey(
                default=django.db.models.query.QuerySet.create,
                on_delete=django.db.models.deletion.CASCADE,
                to="people.adress",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="date_of_birth",
            field=models.DateField(null=True),
        ),
    ]
