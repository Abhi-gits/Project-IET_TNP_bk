from django.urls import path
from . import views


urlpatterns = [
    path("course-list-all/", views.PlacementListAll, name="course-list-all"),
    path("course-list-approved/", views.PlacementListApproved, name="course-list-approved"),
    path("course-create/", views.PlacementCreate.as_view(), name="course-create"),
    path("course-detail/<str:pk>/", views.PlacementDetail.as_view(), name="course-detail"),
    path("course-update/<str:pk>/", views.PlacementUpdate.as_view(), name="course-update"),
    path("course-delete/<str:pk>/", views.PlacementDelete.as_view(), name="course-delete"),
]