from django.contrib import admin
from django.urls import path, include

from src.user import urls as user_urls
from src.hydroponic_system import urls as hydroponic_system_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(user_urls)),
    path("", include(hydroponic_system_urls)),
]
