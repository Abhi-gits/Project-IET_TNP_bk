from django.urls import path, include

urlpatterns = [
    path("", include("api.basic.urls")),
    path('api/account/', include('api.account.urls'))
]
