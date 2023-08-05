from django.urls import path, include

urlpatterns = [
    path('account/', include('api.account.urls')),
    path('placement/', include('api.placement.urls')),
]
