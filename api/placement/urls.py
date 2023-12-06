from django.urls import path
from . import views


urlpatterns = [
    path("", views.PlacementAPIOverview, name="placement-api-overview"),
    path("placement-list-all/", views.PlacementListAll, name="placement-list-all"),
    path("placement-list-approved/", views.PlacementListApproved, name="placement-list-approved"),
    path("placement-create/", views.PlacementCreate, name="placement-create"),
]