from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from src.user import urls as user_urls
from src.hydroponic_system import urls as hydroponic_system_urls


schema_view = get_schema_view(
    openapi.Info(
        title="HydroponicSystem API",
        default_version="1.0.0",
        description="API documentation",
    ),
    public=True,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "swagger/schema/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include(user_urls)),
    path("", include(hydroponic_system_urls)),
]
