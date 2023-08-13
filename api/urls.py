from django.urls import path, include

urlpatterns = [
    path('account/', include('api.account.urls')),
    path('tnp/', include('api.tnp.urls')),
]
