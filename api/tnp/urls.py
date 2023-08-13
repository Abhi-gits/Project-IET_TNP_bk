from django.urls import path, include
from api.tnp.views import PlacementViewSet, PlacementListAPIView, PlacementListAllAPIView, CoursesViewSet, CoursesListAPIView, CoursesListAllAPIView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('placement/create/', PlacementViewSet.as_view({'post': 'create'}), name='create'),
    path('placement/list/', PlacementListAPIView.as_view(), name='list'),
    path('placement/list_all/', PlacementListAllAPIView.as_view(), name='list_all'),
    # Courses urls
    path('courses/create/', CoursesViewSet.as_view({'post': 'create'}), name='create'),
    path('courses/list/', CoursesListAPIView.as_view(), name='list'),
    path('courses/list_all/', CoursesListAllAPIView.as_view(), name='list_all'),
]
