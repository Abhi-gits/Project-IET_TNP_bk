from django.urls import path, include
from api.placement.views import PlacementViewSet, PlacementListAPIView, PlacementListAllAPIView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('create/', PlacementViewSet.as_view({'post': 'create'}), name='create'),
    path('list/', PlacementListAPIView.as_view(), name='list'),
    path('list_all/', PlacementListAllAPIView.as_view(), name='list_all'),

]
