# Generated by Django 4.2.9 on 2024-03-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airplane",
            fields=[
                ("id", models.PositiveIntegerField(primary_key=True, serialize=False)),
                ("fuel_tank_capacity_in_liters", models.PositiveIntegerField()),
                (
                    "fuel_consumption_rate_per_minute",
                    models.DecimalField(decimal_places=4, max_digits=12),
                ),
            ],
        ),
    ]
