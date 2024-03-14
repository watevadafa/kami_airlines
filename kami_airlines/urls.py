from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from airplanes.views import AirplaneViewSet

api_router = DefaultRouter()
api_router.register(r"airplanes", AirplaneViewSet, basename="airplane")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_router.urls)),
]
