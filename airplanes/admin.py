from django.contrib import admin

from airplanes.models import Airplane


@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "fuel_tank_capacity_in_liters",
        "fuel_consumption_rate_per_minute",
    ]
    search_fields = ["id"]
    ordering = ["id"]
    readonly_fields = [
        "fuel_tank_capacity_in_liters",
        "fuel_consumption_rate_per_minute",
    ]
