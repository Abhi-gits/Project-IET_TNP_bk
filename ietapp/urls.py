from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# For JWT Authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("api.basic.urls")),
    path('api/', include('api.urls')),

    # JWT Authentication
    path('api/account/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/account/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # For browsable API
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
