# Generated by Django 5.1.3 on 2024-12-10 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Kitchen_app", "0002_alter_dish_cooks"),
        ("Accounts", "0001_initial")
    ]

    operations = [
        migrations.DeleteModel(
            name="Cook",
        ),
    ]
