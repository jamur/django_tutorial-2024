# Generated by Django 5.0.2 on 2024-02-22 17:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Poll",
            new_name="Question",
        ),
    ]