from django.urls import path
from . import views


urlpatterns = [
    path("placement-list-all/", views.PlacementListAll, name="placement-list-all"),
    path("placement-list-approved/", views.PlacementListApproved, name="placement-list-approved"),
    path("placement-create/", views.PlacementCreate.as_view(), name="placement-create"),
    path("placement-detail/<str:record_id>/", views.PlacementDetail.as_view(), name="placement-detail"),
    path("placement-update/<str:record_id>/", views.PlacementUpdate.as_view(), name="placement-update"),
    path("placement-delete/<str:record_id>/", views.PlacementDelete.as_view(), name="placement-delete"),
]