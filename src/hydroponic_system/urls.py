from rest_framework.routers import DefaultRouter
from django.urls import path, include

from src.hydroponic_system import views as hydroponic_system_views


router = DefaultRouter()
router.register(
    r"hydroponic_system",
    hydroponic_system_views.HydroponicSystemViewSet,
    basename="hydroponic_system",
)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "measurement/",
        hydroponic_system_views.PerformMeasurementView.as_view(),
        name="measurement",
    ),
]
