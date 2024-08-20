# Generated by Django 4.2 on 2024-08-20 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place", models.CharField(max_length=150, verbose_name="место")),
                ("time", models.TimeField(default="12:00:00", verbose_name="время")),
                ("date", models.DateField(blank=True, null=True, verbose_name="дата")),
                ("action", models.CharField(max_length=100, verbose_name="действие")),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=False, verbose_name="признак приятной привычки"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="вознаграждение",
                    ),
                ),
                (
                    "duration",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="длительность выполнения"
                    ),
                ),
                (
                    "periodicity",
                    models.IntegerField(
                        blank=True, default=1, null=True, verbose_name="периодичность"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False, verbose_name="признак публичности"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habit.habit",
                        verbose_name="связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
