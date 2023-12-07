from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


# For JWT Authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("api.basic.urls")),
    path("api/", include("api.urls")),
    # JWT Authentication
    path("api/account/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "api/account/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    # For browsable API
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
    
    # For API Documentation
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]




