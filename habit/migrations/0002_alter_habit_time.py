# Generated by Django 4.2 on 2024-08-20 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="time",
            field=models.TimeField(default="09:00:00", verbose_name="время"),
        ),
    ]
