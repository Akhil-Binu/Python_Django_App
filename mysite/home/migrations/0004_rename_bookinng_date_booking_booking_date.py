# Generated by Django 4.2.5 on 2023-10-11 06:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_booking"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="bookinng_date",
            new_name="booking_date",
        ),
    ]
